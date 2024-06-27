from PySide6.QtWidgets import QDialog

from ui_files.Login_page_ui import Ui_Dialog


class Login_page(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_login.clicked.connect(self.button_clicked)
        self.btn_signup.clicked.connect(self.sign_up_page)

    def button_clicked(self):
        self.text = self.user_name_lineEdit.text()
        if self.text:
            self.accept()

    def sign_up_page(self):
        self.stackedWidget.setCurrentIndex(1)
