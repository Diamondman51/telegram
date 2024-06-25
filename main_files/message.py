from PySide6.QtWidgets import QWidget

from ui_files.message_ui import Ui_Form


class Message(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
