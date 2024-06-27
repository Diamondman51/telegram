import errno
import socket
import sqlite3

from PySide6.QtCore import Signal, QThread

HEADER = 10
IP = 'localhost'
PORT = 1234



class DataBase(QThread):
    received = Signal(tuple)

    def __init__(self, ip=IP, port=PORT):
        super().__init__()
        self.ip = ip
        self.port = port
        self.running = False

    def run(self):

        self.running = True
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.connect((self.ip, self.port))
        self.my_socket.setblocking(True)

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

    def receive_message(self):
        print('receive_message')
        username_header = self.my_socket.recv(HEADER)
        print(123)
        if not len(username_header):
            self.running = False

        message_length = int(username_header.decode('utf-8'))
        full_message = self.my_socket.recv(message_length).decode('utf-8')

        print('full_message', full_message)

        username = full_message.split()[0]
        message = full_message[len(username):]

        self.received.emit((username, message))
        print('signal emited', username, message)


    def send_message(self, username: str, message: str):
        print('send_message')
        if self.running and self.my_socket:
            try:
                message = f'{username} {message}'.encode('utf-8')
                message_header = f"{len(f'{message}'):<{HEADER}}".encode('utf-8')
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
