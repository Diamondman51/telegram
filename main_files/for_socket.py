import socket
import sqlite3
import sys
import threading

from PyQt5.QtCore import QThread

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = 'localhost'
PORT = 1234

my_socket.connect((IP, PORT))
my_socket.setblocking(True)

HEADER = 10


class DataBase(QThread):
    def __init__(self, username: str, main_window):
        print(123)
        self.main_window = main_window
        self.username = username.encode('utf-8')
        self.username_length = f"{len(username):<{HEADER}}".encode('utf-8')
        my_socket.send(self.username_length + self.username)

        print('st')
        self.main_window.btn_send_message.clicked.connect(self.send_m)
        print('end')

        self.send_thread = threading.Thread(target=self.send_message, args=(self.main_window.message_lineEdit.text(),))
        receive_thread = threading.Thread(target=self.receive_message)

        receive_thread.start()
        receive_thread.join()
        my_socket.close()

    def send_m(self):
        print(456)

        send_thread = threading.Thread(target=self.send_message, args=(self.main_window.message_lineEdit.text(),))
        if self.main_window.message_lineEdit.text():
            self.main_window.send_message_main(self.main_window.username_LineEdit.text(), self.main_window.message_LineEdit.text())
            print(self.main_window.username_LineEdit.text(), self.main_window.message_LineEdit.text())
        send_thread.start()
        send_thread.join()

    def receive_message(self):
        while True:
            username_header = my_socket.recv(HEADER)
            if not len(username_header):
                sys.exit()

            username_length = int(username_header.decode('utf-8'))
            username = my_socket.recv(username_length).decode('utf-8')

            message_header = my_socket.recv(HEADER)
            message_length = int(message_header.decode('utf-8'))
            message = my_socket.recv(message_length).decode('utf-8')

            if self.main_window.message_lineEdit:
                self.main_window.send_message_main(username, message)
            # return username, message

    def send_message(self, message):
        while True:
            try:
                if message:
                    message = message.encode('utf-8')
                    message_header = f"{len(message):<{HEADER}}".encode('utf-8')
                    my_socket.send(message_header + message)
            except (OSError, BrokenPipeError):
                break

    def save_data(self, user_name):
        with sqlite3.connect('mydb.db') as db:
            query = '''create table if not exists mydata (
                        username varchar not null
                        )
                    '''
            db.execute(query)
            db.commit()

            query = '''insert into mydata 
                    values (%s)'''

            db.execute(query, (user_name, ))
            db.commit()
