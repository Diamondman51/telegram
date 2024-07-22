import errno
import socket

from PySide6.QtCore import QThread, Signal

HEADER_LENGTH = 10
IP = "localhost"
PORT = 1234


class ClientSocket(QThread):
    # received = Signal(list)
    received = Signal(list)
    def __init__(self, ip=IP, port=PORT, parent=None):
        super().__init__()
        self.ip = ip
        self.port = port
        self.running = False

    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        # print('run')
        self.running = True
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))
        self.client_socket.setblocking(True)

        while self.running:
            try:
                print('run')
                self.receive_message()
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("Reading error", e)
                    break
            except Exception as e:
                print('General error', e)
                break

    def receive_message(self):
        print('receive_message activated')
        username_header = self.client_socket.recv(HEADER_LENGTH)
        print('123')
        if not len(username_header):
            self.running = False

        length = int(username_header.decode('utf-8'))
        full_message = self.client_socket.recv(length).decode('utf-8')
        # print(full_message.split()[0])
        username = full_message.split()[0]
        message = full_message.split()[1:]

        print('full_message', full_message)

        self.received.emit([username, message])
        print(f'username: {username}, message: {message}')
        return {'username': username, 'message': message}

    def send_message(self, username, message):
        # print('send_message')
        """Handles sending messages to the server."""
        if self.client_socket and self.running:
            try:
                message = f'{username} {message}'.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                self.client_socket.send(message_header + message)
            except (OSError, BrokenPipeError):
                print("Disconnected from server.")
                self.running = False

    def stop(self):
        """Stops the thread and closes the connection."""
        self.running = False
        self.quit()
        self.wait()
