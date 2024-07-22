import time

from PySide6.QtCore import Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem, QLabel

from main_files.Dialog_for_each_user import Dialog_for_each_user
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
        self.widget_2.setHidden(True)
        self.users_listWidget.itemClicked.connect(self.send_to_selected_user)
        self.data.received.connect(self.receive_message_main)
        self.data.new_user.connect(self.add_to_users)
        self.data.delete.connect(self.delete_user)
        self.list_of_users = []
        self.btn_menu_1.clicked.connect(self.menu_clicked)
        self.btn_menu_2.clicked.connect(self.menu_clicked)

    def send_to_selected_user(self):
        item = self.users_listWidget.currentItem()
        widget = self.users_listWidget.itemWidget(item)
        self.to = widget.label.text()

        self.user_widget.dialog.btn_send_message.clicked.connect(self.send_message_main)
        self.stackedWidget.setCurrentWidget(self.user_widget.dialog)

    def send_message_main(self):
        # print(123)
        message_widget = Message('right')
        message_widget.message_label.setAlignment(Qt.AlignRight)
        message_widget.username_label.setAlignment(Qt.AlignRight)

        if self.user_widget.dialog.message_lineEdit.toPlainText():
            message = self.user_widget.dialog.message_lineEdit.toPlainText()
            username = self.username_LineEdit.text()
            # to = self.users_listWidget

            message_widget.message_label.setText(message)
            message_widget.username_label.setText(username)
            message_widget.adjust_text_edit_size()

            item = QListWidgetItem()
            item.setSizeHint(message_widget.sizeHint())
            self.user_widget.dialog.listWidget_for_messages.addItem(item)
            self.user_widget.dialog.listWidget_for_messages.setItemWidget(item, message_widget)

            # self.cl_sock.send_message(self.username_LineEdit.text(), message)
            self.data.send_message(username, message, self.to)
            self.user_widget.dialog.message_lineEdit.clear()

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
        self.user_widget.dialog.listWidget_for_messages.addItem(item)
        self.user_widget.dialog.listWidget_for_messages.setItemWidget(item, message_widget)
        print('main clients', type(full_message['users']))
        print('main 2 full_message', full_message)
        if full_message['type'] == 2:
            print('________________Changed________________')
            # self.stackedWidget.setCurrentWidget(self.user_widget.dialog)
            #
            # if full_message['from']
            # self.users_listWidget.setFocus()
        self.add_to_users(full_message)
        # TODO finish counting new messages
        n_of_messages = self.user_widget.dialog.listWidget_for_messages.count()

    def send_message_login(self, username, message):
        self.data.send_message(username, message)

    def add_to_users(self, full_message):

        print('\n', 'full_message: ', full_message, '\n')
        for user in full_message['users']:
            if user not in self.list_of_users and user != self.username_LineEdit.text():

                self.user_widget = Add_User()

                self.user_widget.label.setText(user)
                self.user_widget.label.setStyleSheet('color: black; font-size: 24px; padding: 8')
                self.user_widget.label.adjustSize()
                item = QListWidgetItem()
                item.setSizeHint(self.user_widget.label.sizeHint())
                self.users_listWidget.addItem(item)
                self.users_listWidget.setItemWidget(item, self.user_widget)
                self.list_of_users.append(user)
                print('main self.add_to_users()', self.list_of_users)
                self.stackedWidget.addWidget(self.user_widget.dialog)

    def delete_user(self, full_message):
        for row in range(len(self.list_of_users)):
            if full_message['from'] == self.list_of_users[row]:
                del self.list_of_users[row]
            item = self.users_listWidget.item(row)
            widget = self.users_listWidget.itemWidget(item)
            if widget.label.text() == full_message['from']:
                # self.users_listWidget.takeItem(self.users_listWidget.row(item))
                self.users_listWidget.takeItem(row)
                self.stackedWidget.removeWidget(self.user_widget.dialog)

    def menu_clicked(self, flag):
        self.btn_menu_1.setChecked(not flag)
        self.btn_menu_2.setChecked(not flag)


class Add_User(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.dialog = Dialog_for_each_user()
