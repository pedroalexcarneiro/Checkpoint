"""Botões do Switch Pro por SDL3/HIDAPI, consultados pela thread do Qt."""
import ctypes as c
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import sys


SDL_DLL=Path(__file__).parent/'assets'/'sdl3'/'SDL3.dll'
GAMEPAD_SUBSYSTEM=0x2000
SWITCH_PRO=7
SDL_CAPTURE_BUTTON=15
CAPTURE_MASK=0x0400
# SDL_GamepadButton -> máscara já usada pelo diálogo de captura.
BUTTON_MAP={11:0x0001,12:0x0002,13:0x0004,14:0x0008,6:0x0010,4:0x0020,
            7:0x0040,8:0x0080,9:0x0100,10:0x0200,SDL_CAPTURE_BUTTON:CAPTURE_MASK,
            1:0x1000,0:0x2000,3:0x4000,2:0x8000}


@dataclass(frozen=True)
class SwitchDevice:
    name: str
    instance: int
    buttons: int


class SwitchControllers:
    def __init__(self,dll):
        self.dll=dll
        self.opened={}
        self.active=False
        arguments={
            'SDL_SetHint':(c.c_bool,c.c_char_p,c.c_char_p),
            'SDL_InitSubSystem':(c.c_bool,c.c_uint32),
            'SDL_QuitSubSystem':(None,c.c_uint32),
            'SDL_SetGamepadEventsEnabled':(None,c.c_bool),
            'SDL_UpdateGamepads':(None,),
            'SDL_GetGamepads':(c.POINTER(c.c_uint32),c.POINTER(c.c_int)),
            'SDL_free':(None,c.c_void_p),
            'SDL_GetRealGamepadTypeForID':(c.c_int,c.c_uint32),
            'SDL_OpenGamepad':(c.c_void_p,c.c_uint32),
            'SDL_CloseGamepad':(None,c.c_void_p),
            'SDL_GamepadConnected':(c.c_bool,c.c_void_p),
            'SDL_GamepadHasButton':(c.c_bool,c.c_void_p,c.c_int),
            'SDL_GetGamepadButton':(c.c_bool,c.c_void_p,c.c_int),
            'SDL_GetGamepadSerial':(c.c_char_p,c.c_void_p),
            'SDL_GetGamepadPath':(c.c_char_p,c.c_void_p),
            'SDL_GetGamepadVendor':(c.c_uint16,c.c_void_p),
            'SDL_GetGamepadProduct':(c.c_uint16,c.c_void_p),
            'SDL_GetGamepadConnectionState':(c.c_int,c.c_void_p),
        }
        for name,(result,*args) in arguments.items():
            function=getattr(dll,name)
            function.restype=result
            function.argtypes=args
        dll.SDL_SetHint(b'SDL_JOYSTICK_HIDAPI_SWITCH',b'1')
        dll.SDL_SetHint(b'SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS',b'1')
        if not dll.SDL_InitSubSystem(GAMEPAD_SUBSYSTEM):
            raise OSError('Não foi possível iniciar a leitura do Switch Pro.')
        self.active=True
        dll.SDL_SetGamepadEventsEnabled(False)

    @classmethod
    def windows(cls):
        if sys.platform!='win32' or not SDL_DLL.is_file():
            raise OSError('Leitura do Switch Pro indisponível.')
        return cls(c.CDLL(str(SDL_DLL),winmode=0x900))

    def open_switch(self,instance):
        dll=self.dll
        if dll.SDL_GetRealGamepadTypeForID(instance)!=SWITCH_PRO:return
        handle=dll.SDL_OpenGamepad(instance)
        if not handle:return
        serial=dll.SDL_GetGamepadSerial(handle)
        path=dll.SDL_GetGamepadPath(handle)
        identity=b'serial:'+serial.lower() if serial else b'path:'+path.lower() if path else None
        if not identity or not dll.SDL_GamepadHasButton(handle,SDL_CAPTURE_BUTTON):
            dll.SDL_CloseGamepad(handle)
            return
        vendor=dll.SDL_GetGamepadVendor(handle)
        product=dll.SDL_GetGamepadProduct(handle)
        device='switch:'+sha256(f'{vendor:04x}:{product:04x}:'.encode()+identity).hexdigest()
        connection=dll.SDL_GetGamepadConnectionState(handle)
        name={1:'Switch Pro · USB',2:'Switch Pro · sem fio'}.get(connection,'Switch Pro')
        self.opened[instance]=(handle,device,name)

    def devices(self):
        dll=self.dll
        dll.SDL_UpdateGamepads()
        count=c.c_int()
        ids=dll.SDL_GetGamepads(c.byref(count))
        try:connected={ids[i] for i in range(count.value)} if ids else set()
        finally:
            if ids:dll.SDL_free(ids)
        for instance in self.opened.keys()-connected:
            dll.SDL_CloseGamepad(self.opened.pop(instance)[0])
        for instance in connected-self.opened.keys():self.open_switch(instance)
        devices={}
        for instance,(handle,device,name) in self.opened.items():
            if not dll.SDL_GamepadConnected(handle):continue
            buttons=sum(mask for button,mask in BUTTON_MAP.items() if dll.SDL_GetGamepadButton(handle,button))
            # Um mesmo número de série pode ser exposto por dois transportes.
            devices[device]=None if device in devices else SwitchDevice(name,instance,buttons)
        return {device:state for device,state in devices.items() if state is not None}

    def close(self):
        if not self.active:return
        for handle,_,_ in self.opened.values():self.dll.SDL_CloseGamepad(handle)
        self.opened.clear()
        self.dll.SDL_QuitSubSystem(GAMEPAD_SUBSYSTEM)
        self.active=False
