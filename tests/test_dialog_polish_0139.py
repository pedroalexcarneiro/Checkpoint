from pathlib import Path
import subprocess
from PySide6.QtCore import Qt,QTimer
from PySide6.QtWidgets import QApplication,QMessageBox,QInputDialog,QDialogButtonBox
from checkpoint.dialog_style import AppMessages,AppInputs,FittedImage
from test_bugs_0134 import ui,sample


def observe_modal(window, callback):
    captured={}
    timer=QTimer(window);timer.setSingleShot(True)
    def inspect():
        modal=QApplication.activeModalWidget()
        if modal is None:captured['error']='Nenhum modal';return
        captured['title']=modal.windowTitle()
        captured['prepared']=getattr(modal,'_checkpoint_presentation',None) is not None
        captured['buttons']=[b.text().replace('&','') for box in modal.findChildren(QDialogButtonBox) for b in box.buttons()]
        captured['size']=modal.size()
        captured['geometry']=modal.frameGeometry()
        captured['screen']=modal.screen().availableGeometry()
        if isinstance(modal,QMessageBox):
            captured['default']=modal.defaultButton().text().replace('&','') if modal.defaultButton() else None
            modal.button(QMessageBox.No).click()
        else:modal.reject()
    timer.timeout.connect(inspect);timer.start(25)
    result=callback()
    timer.stop();timer.deleteLater()
    assert 'error' not in captured
    return result,captured


def test_standard_question_theme_portuguese_default_and_cancellation(ui):
    w,_=ui
    result,captured=observe_modal(w,lambda:AppMessages.question(w,'Remover registro','Confirmar ação de teste?'))
    assert result==QMessageBox.No
    assert set(captured['buttons'])=={'Sim','Não'}
    assert captured['default']=='Não' and captured['prepared']
    assert captured['screen'].contains(captured['geometry'])


def test_session_prompt_has_explicit_actions_and_safe_default(ui):
    w,_=ui
    result,captured=observe_modal(w,lambda:AppMessages.start_session(w))
    assert result==QMessageBox.No
    assert captured['title']=='Iniciar sessão?'
    assert set(captured['buttons'])=={'Cancelar','Iniciar sessão'}
    assert captured['default']=='Cancelar'


def test_standard_input_translates_cancel_without_changing_selection(ui):
    w,_=ui
    result,captured=observe_modal(w,lambda:AppInputs.getItem(w,'Selecionar perfil','Perfil:',['Perfil A','Perfil B'],0,False))
    assert result[1] is False
    assert 'Cancelar' in captured['buttons'] and 'Cancel' not in captured['buttons']
    assert captured['prepared']


def test_authorized_image_viewer_keeps_image_proportions_and_original(ui,app,folder):
    from checkpoint.dialogs import ImageDialog
    from PySide6.QtGui import QImage,QColor
    path=folder/'Minha captura.png'
    image=QImage(400,240,QImage.Format_RGB32);image.fill(QColor('#aadd44'));assert image.save(str(path))
    original=path.read_bytes()
    dialog=ImageDialog(str(path),ui[0]);dialog.show()
    try:
        for size in ((600,400),(1000,750),(500,300)):
            dialog.resize(*size)
            for _ in range(8):app.processEvents()
            fitted=dialog.findChild(FittedImage)
            pix=fitted.pixmap()
            assert not pix.isNull()
            assert abs(pix.width()/pix.height()-400/240)<.03
            assert pix.width()<=fitted.width() and pix.height()<=fitted.height()
        assert path.read_bytes()==original
    finally:dialog.reject()


def test_only_authorized_protected_constructor_changed():
    filename='checkpoint/dialogs.py'
    base=subprocess.check_output(['git','show','9dd9c93:'+filename])
    current=Path(filename).read_bytes()
    marker=b'class ImageDialog(QDialog):'
    assert base.split(marker)[0]==current.split(marker)[0]
