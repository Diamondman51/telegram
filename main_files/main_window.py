from PySide6.QtCore import Signal
from PySide6.QtGui import Qt, QColor, QBrush
from PySide6.QtWidgets import QWidget, QListWidgetItem

from main_files.for_socket import DataBase
from main_files.message import Message
from ui_files.main_window_ui import Ui_Form


class Main_Window(Ui_Form, QWidget):
    text_setted = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.cl_sock = ClientSocket()
        self.data = DataBase()
        self.data.start()
        self.btn_menu_2.setChecked(True)
        self.btn_send_message.clicked.connect(self.send_message_main)
        self.username_LineEdit.setText('Java')
        # self.cl_sock.received.connect(self.receive_message_main)
        self.data.received.connect(self.receive_message_main)
        # self.cl_sock.start()

    def send_message_main(self):
        # print(123)
        message_widget = Message('right')
        message_widget.message_label.setAlignment(Qt.AlignRight)
        message_widget.username_label.setAlignment(Qt.AlignRight)

        if self.message_lineEdit.text():
            message = self.message_lineEdit.text()
            username = self.username_LineEdit.text()

            message_widget.message_label.setText(message)
            message_widget.username_label.setText(username)
            message_widget.adjust_text_edit_size()

            item = QListWidgetItem()
            item.setSizeHint(message_widget.sizeHint())
            self.listWidget_for_messages.addItem(item)
            self.listWidget_for_messages.setItemWidget(item, message_widget)

            # self.cl_sock.send_message(self.username_LineEdit.text(), message)
            self.data.send_message(self.username_LineEdit.text(), message)

    def receive_message_main(self, full_message):
        print('full_message', full_message)
        message_widget = Message('left')
        message_widget.username_label.setAlignment(Qt.AlignLeft )
        message_widget.message_label.setAlignment(Qt.AlignLeft)
        message_widget.username_label.setText(full_message[0])
        message_widget.message_label.setText((full_message[1]))
        message_widget.adjust_text_edit_size()

        item = QListWidgetItem()

        item.setSizeHint(message_widget.sizeHint())
        self.listWidget_for_messages.addItem(item)
        self.listWidget_for_messages.setItemWidget(item, message_widget)

    def send_message_login(self, username, message):
        self.data.send_message(username, message)
        # message_widget = QLabel()
        # message_widget.setText(f'{username} {message}')
        # item.foreground()
        item = QListWidgetItem()
        item.setText(f'{username} {message}')
        # item.
        item.setForeground(QColor('white'))
        item.setBackground(QColor('rgb(92, 157, 255)'))
        item.setTextAlignment(Qt.AlignCenter)
        self.listWidget_for_messages.addItem(item)
