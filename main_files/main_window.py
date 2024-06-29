import time

from PySide6.QtCore import Signal
from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import QWidget, QListWidgetItem, QLabel

from main_files.for_socket import DataBase
from main_files.message import Message
from ui_files.main_window_ui import Ui_Form


class Main_Window(Ui_Form, QWidget):
    text_setted = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = DataBase()
        self.data.start()
        time.sleep(0.01)
        self.btn_menu_2.setChecked(True)
        self.users_listWidget.itemClicked.connect(self.send_to_selected_user)
        self.data.received.connect(self.receive_message_main)
        self.data.new_user.connect(self.add_to_users)
        self.list_of_users = []

    def send_to_selected_user(self):
        item = self.users_listWidget.currentItem()
        widget = self.users_listWidget.itemWidget(item)
        self.to = widget.label.text()

        self.btn_send_message.clicked.connect(self.send_message_main)

    def send_message_main(self):
        # print(123)
        message_widget = Message('right')
        message_widget.message_label.setAlignment(Qt.AlignRight)
        message_widget.username_label.setAlignment(Qt.AlignRight)

        if self.message_lineEdit.text():
            message = self.message_lineEdit.text()
            username = self.username_LineEdit.text()
            # to = self.users_listWidget

            message_widget.message_label.setText(message)
            message_widget.username_label.setText(username)
            message_widget.adjust_text_edit_size()

            item = QListWidgetItem()
            item.setSizeHint(message_widget.sizeHint())
            self.listWidget_for_messages.addItem(item)
            self.listWidget_for_messages.setItemWidget(item, message_widget)

            # self.cl_sock.send_message(self.username_LineEdit.text(), message)
            self.data.send_message(username, message, self.to)

    def receive_message_main(self, full_message: dict):
        print('full_message', full_message)
        message_widget = Message('left')
        message_widget.username_label.setAlignment(Qt.AlignLeft)
        message_widget.message_label.setAlignment(Qt.AlignLeft)
        message_widget.username_label.setText(full_message['from'])
        message_widget.message_label.setText((full_message['message']))
        message_widget.adjust_text_edit_size()

        item = QListWidgetItem()

        item.setSizeHint(message_widget.sizeHint())
        self.listWidget_for_messages.addItem(item)
        self.listWidget_for_messages.setItemWidget(item, message_widget)
        print('main clients', full_message['clients'])
        for user in full_message['users']:
            # if full_message['from'] not in self.list_of_users:
            if user not in self.list_of_users:
                self.list_of_users.append(user)
                self.add_to_users(user)

    def send_message_login(self, username, message):
        self.data.send_message(username, message)
        # message_widget = QLabel()
        # message_widget.setText(f'{username} {message}')
        # item.foreground()

        # item = QListWidgetItem()
        # item.setText(f'{username} {message}')
        # # item.
        # item.setForeground(QColor('white'))
        # item.setBackground(QColor('rgb(92, 157, 255)'))
        # item.setTextAlignment(Qt.AlignCenter)
        # self.listWidget_for_messages.addItem(item)

    def add_to_users(self, user_name):
        print('main self.add_to_users()', user_name)
        widget = Add_User()
        widget.label.setText(user_name)
        widget.label.setStyleSheet('color: black; font-size: 24px; padding: 8')
        widget.label.adjustSize()
        item = QListWidgetItem()
        item.setSizeHint(widget.label.sizeHint())
        self.users_listWidget.addItem(item)
        self.users_listWidget.setItemWidget(item, widget)
        self.list_of_users.append(user_name)


class Add_User(QWidget):
    def __init__(self):
        super().__init__()
        # widget = QWidget()
        self.label = QLabel(self)
