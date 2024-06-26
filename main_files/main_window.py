from time import sleep

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem

from client_socket import ClientSocket
from main_files.message import Message
from ui_files.main_window_ui import Ui_Form


class Main_Window(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cl_sock = ClientSocket()
        self.btn_menu_2.setChecked(True)
        self.btn_send_message.clicked.connect(self.send_message_main)
        self.username_LineEdit.setText('Java')
        # data = DataBase(self.username_LineEdit.text(), self)
        self.cl_sock.received.connect(self.receive_message_main)
        self.cl_sock.start()

    def send_message_main(self):
        # print(123)
        message_widget = Message()
        message_widget.message_label.setAlignment(Qt.AlignRight)
        message_widget.username_label.setAlignment(Qt.AlignRight)

        if self.message_lineEdit:
            message = self.message_lineEdit.text()
            username = self.username_LineEdit.text()

            message_widget.message_label.setText(message)
            message_widget.username_label.setText(username)

            item = QListWidgetItem()
            item.setSizeHint(message_widget.sizeHint())
            self.listWidget_for_messages.addItem(item)
            self.listWidget_for_messages.setItemWidget(item, message_widget)
            # if not self.cl_sock.isRunning():
            #     self.cl_sock.run()

            self.cl_sock.send_message(self.username_LineEdit.text(), message)
            # data = DataBase(self.username_LineEdit.text())
            # data.send_message(self.message_lineEdit.text())

    def receive_message_main(self, full_message):
        print("receive_main", full_message[0], full_message[1])
        message_widget = Message()
        message_widget.message_label.setAlignment(Qt.AlignLeft)
        message_widget.username_label.setAlignment(Qt.AlignLeft )
        message_widget.username_label.setText(full_message[0])
        message_widget.message_label.setText(full_message[1])

        item = QListWidgetItem()

        item.setSizeHint(message_widget.sizeHint())
        self.listWidget_for_messages.addItem(item)
        self.listWidget_for_messages.setItemWidget(item, message_widget)
