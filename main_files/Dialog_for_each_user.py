from PySide6.QtWidgets import QWidget

from ui_files.stackedWidget_dialog_for_each_user_ui import Ui_Form


class Dialog_for_each_user(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
