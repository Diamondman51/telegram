import errno
import json
import socket
import sqlite3

from PySide6.QtCore import Signal, QThread

from filter_messages import filtering

HEADER = 10
IP = 'localhost'
PORT = 1234


class DataBase(QThread):
    new_user = Signal(str)
    received = Signal(dict)

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    my_socket.setblocking(True)

    def __init__(self, ip=IP, port=PORT):
        super().__init__()
        self.ip = ip
        self.port = port
        self.running = False

    def run(self):

        self.running = True

        while self.running:
            try:
                print('run')
                self.receive_message()
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('reading error')
                    break
            except Exception as e:
                print('General error', e)
                break

    flag_1 = False

    def receive_message(self):
        print('receive_message')

        message_length = self.my_socket.recv(HEADER)

        print(123)
        if not len(message_length):
            self.running = False

        # Emit new user
        # if not self.flag_1:
        #     new_user = self.my_socket.recv(int(username_header.decode()))
        #     self.new_user.emit(new_user)
        #     DataBase.flag_1 = True

        print('rc username_header.decode()', message_length)
        message_length = int(message_length.decode('utf-8'))
        print('rc message_length', message_length)
        full_message: bytes = self.my_socket.recv(message_length)
        print('rc full_message', type(full_message), full_message)

        full_message: dict = json.loads(full_message)
        print('rc full_message 2: ', type(full_message), full_message)

        if full_message['type'] == 0:
            # full_message['users']

            return self.new_user.emit(full_message)

        print('rc full_message', full_message, message_length)

        self.received.emit(full_message)
        print('rc signal emited', full_message)

    flag_2 = False

    def send_message(self, username: str, message: str = None, to=None):
        print('send_message')

        if message and self.running and self.my_socket:
            try:
                data_type = 1
                if not self.flag_2:
                    data_type = 0
                    DataBase.flag_2 = True
                message = filtering(username, message, to=to, data_type=data_type)
                message_header = f"{len(f'{message}'):<{HEADER}}".encode('utf-8')
                print('my_socket.send(message_header + message)', message_header.decode() + ' ' + message.decode())
                self.my_socket.send(message_header + message)
            except (OSError, BrokenPipeError) as error:
                print('Error: ', error)
                self.running = False

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

    def stop(self):
        self.running = False
