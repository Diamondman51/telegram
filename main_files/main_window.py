from PySide6.QtWidgets import QWidget, QListWidgetItem

from client_socket import ClientSocket
from main_files.message import Message
from ui_files.main_window_ui import Ui_Form
from main_files.for_socket import DataBase


class Main_Window(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_menu_2.setChecked(True)
        self.btn_send_message.clicked.connect(self.send_message_main)
        self.username_LineEdit.setText('Java')
        # data = DataBase(self.username_LineEdit.text(), self)
        self.cl_sock = ClientSocket(self.username_LineEdit.text(), 'localhost', 1234)

    def send_message_main(self):
        message_widget = Message()

        if self.message_lineEdit:
            message = message_widget.message_label.setText(self.message_lineEdit.text())
            username = message_widget.username_label.setText(self.username_LineEdit.text())

            message_widget.message_label.setText(message)
            message_widget.username_label.setText(username)

            item = QListWidgetItem()
            item.setSizeHint(message_widget.sizeHint())
            self.listWidget_for_messages.addItem(item)
            self.listWidget_for_messages.setItemWidget(item, message_widget)
            if not self.cl_sock.isRunning():
                self.cl_sock.start()
            self.cl_sock.send_message(message)
            # data = DataBase(self.username_LineEdit.text())
            # data.send_message(self.message_lineEdit.text())
