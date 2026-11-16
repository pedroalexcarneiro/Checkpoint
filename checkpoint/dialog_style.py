"""Apresentação opt-in de diálogos; sem filtro global ou seletores nativos."""
from PySide6.QtCore import QObject, QEvent, QPoint, QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QMessageBox, QInputDialog,
    QWidget, QLabel, QSizePolicy)
from .design_system import colors
from .icons import lucide_icon

BUTTONS = {
    'OK': 'OK', 'Cancel': 'Cancelar', 'Close': 'Fechar', 'Yes': 'Sim', 'No': 'Não',
    'Save': 'Salvar', 'Open': 'Abrir', 'Apply': 'Aplicar', 'Retry': 'Tentar novamente',
    'Abort': 'Cancelar', 'Ignore': 'Ignorar', 'Reset': 'Redefinir', 'Help': 'Ajuda'}


class DialogPresentation(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Show and isinstance(obj, QDialog):
            self.present(obj)
        return False

    def present(self, dialog):
        if isinstance(dialog, QMessageBox):
            dialog.setOption(QMessageBox.DontUseNativeDialog, True)
            name = 'warning' if dialog.icon() in (QMessageBox.Warning, QMessageBox.Critical) else 'help'
            dialog.setIconPixmap(lucide_icon(name, colors()['accent'], 32).pixmap(32, 32))
        for box in dialog.findChildren(QDialogButtonBox):
            for button in box.buttons():
                raw = button.text().replace('&', '')
                if raw in BUTTONS:
                    button.setText(BUTTONS[raw])
        if isinstance(dialog,QMessageBox):
            for standard,label in getattr(dialog,'_checkpoint_button_labels',{}).items():
                button=dialog.button(standard)
                if button:button.setText(label)
        parent = dialog.parentWidget()
        if parent:
            host = parent.window()
            if not host.windowIcon().isNull():
                dialog.setWindowIcon(host.windowIcon())
            screen = host.screen()
            center = host.mapToGlobal(host.rect().center())
        else:
            screen = dialog.screen()
            center = screen.availableGeometry().center()
        area = screen.availableGeometry().adjusted(16, 16, -16, -16)
        dialog.setMaximumSize(area.size())
        width = min(dialog.width(), area.width())
        height = min(dialog.height(), area.height())
        dialog.resize(width, height)
        x = max(area.left(), min(area.right()-dialog.width()+1, center.x()-dialog.width()//2))
        y = max(area.top(), min(area.bottom()-dialog.height()+1, center.y()-dialog.height()//2))
        dialog.move(x, y)
        if dialog.windowHandle():
            from .window_style import titlebar_theme
            titlebar_theme(dialog, True)


def prepare_dialog(dialog):
    """Não abre HWND durante a construção; trata apenas Show do próprio modal."""
    if getattr(dialog, '_checkpoint_presentation', None) is None:
        # Construir um QObject filho pode provocar Polish reentrante no pai.
        dialog._checkpoint_presentation = False
        guard = DialogPresentation(dialog)
        dialog._checkpoint_presentation = guard
        dialog.installEventFilter(guard)
    return dialog


class AppMessages(QMessageBox):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setOption(QMessageBox.DontUseNativeDialog,True)
        prepare_dialog(self)
    @staticmethod
    def _message(icon,parent,title,message,buttons=QMessageBox.Ok,defaultButton=QMessageBox.NoButton,labels=None):
        box=AppMessages(parent);box.setWindowTitle(title);box.setText(message)
        box.setIcon(icon);box.setStandardButtons(buttons)
        box._checkpoint_button_labels=labels or {}
        if defaultButton!=QMessageBox.NoButton:box.setDefaultButton(defaultButton)
        if buttons & QMessageBox.No:box.setEscapeButton(QMessageBox.No)
        elif buttons & QMessageBox.Cancel:box.setEscapeButton(QMessageBox.Cancel)
        return box.exec()
    @staticmethod
    def start_session(parent):
        message='Este emulador não detecta quando você fecha apenas a ROM.\nAo terminar, encerre o registro da sessão manualmente.'
        return AppMessages.question(parent,'Iniciar sessão?',message,
            QMessageBox.Yes|QMessageBox.No,QMessageBox.No,{QMessageBox.Yes:'Iniciar sessão',QMessageBox.No:'Cancelar'})
    @staticmethod
    def question(parent,title,message,buttons=QMessageBox.Yes|QMessageBox.No,defaultButton=QMessageBox.No,labels=None):
        return AppMessages._message(QMessageBox.Question,parent,title,message,buttons,defaultButton,labels)
    @staticmethod
    def information(parent,title,message,buttons=QMessageBox.Ok,defaultButton=QMessageBox.NoButton):
        return AppMessages._message(QMessageBox.Information,parent,title,message,buttons,defaultButton)
    @staticmethod
    def warning(parent,title,message,buttons=QMessageBox.Ok,defaultButton=QMessageBox.NoButton):
        return AppMessages._message(QMessageBox.Warning,parent,title,message,buttons,defaultButton)
    @staticmethod
    def critical(parent,title,message,buttons=QMessageBox.Ok,defaultButton=QMessageBox.NoButton):
        return AppMessages._message(QMessageBox.Critical,parent,title,message,buttons,defaultButton)


class AppInputs(QInputDialog):
    def __init__(self,parent=None):
        super().__init__(parent);self.setOkButtonText('Confirmar');self.setCancelButtonText('Cancelar')
        prepare_dialog(self)
    @staticmethod
    def getItem(parent,title,label,items,current=0,editable=True):
        dialog=AppInputs(parent);dialog.setWindowTitle(title);dialog.setLabelText(label)
        dialog.setComboBoxItems(items);dialog.setComboBoxEditable(editable)
        if items:dialog.setTextValue(items[max(0,min(len(items)-1,current))])
        accepted=dialog.exec()==QDialog.Accepted
        return dialog.textValue(),accepted
    @staticmethod
    def getText(parent,title,label,echo=None,text=''):
        from PySide6.QtWidgets import QLineEdit
        dialog=AppInputs(parent);dialog.setWindowTitle(title);dialog.setLabelText(label)
        dialog.setInputMode(QInputDialog.TextInput);dialog.setTextEchoMode(QLineEdit.Normal if echo is None else echo)
        dialog.setTextValue(text);accepted=dialog.exec()==QDialog.Accepted
        return dialog.textValue(),accepted
    @staticmethod
    def getInt(parent,title,label,value=0,minValue=-2147483647,maxValue=2147483647,step=1):
        dialog=AppInputs(parent);dialog.setWindowTitle(title);dialog.setLabelText(label)
        dialog.setInputMode(QInputDialog.IntInput);dialog.setIntRange(minValue,maxValue);dialog.setIntStep(step);dialog.setIntValue(value)
        accepted=dialog.exec()==QDialog.Accepted
        return dialog.intValue(),accepted


class FittedImage(QLabel):
    def __init__(self,path):
        super().__init__();self.source=QPixmap(path);self.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(0,0);self.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)
    def resizeEvent(self,event):
        super().resizeEvent(event)
        self.setPixmap(self.source.scaled(self.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
