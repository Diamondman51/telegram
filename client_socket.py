import errno
import socket
import sys
from PySide6.QtCore import QThread, Signal, Slot, Qt

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234


class ClientSocket(QThread):
    received = Signal(str)
    connected = Signal()
    disconnected = Signal()

    def __init__(self, username, ip=IP, port=PORT, parent=None):
        super().__init__(parent)
        self.username = username
        self.ip = ip
        self.port = port
        self.client_socket = None
        self.running = False

    def run(self):
        """Main thread execution function."""
        self.running = True
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))
        self.client_socket.setblocking(True)

        username = self.username.encode('utf-8')
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(username_header + username)

        self.connected.emit()  # Emit connected signal

        while self.running:
            try:
                self.receive_messages()
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print("Reading error", e)
                    break
            except Exception as e:
                print('General error', e)
                break

        self.disconnected.emit()  # Emit disconnected signal
        self.client_socket.close()

    @Slot(str)
    def send_message(self, message):
        """Handles sending messages to the server."""
        if self.client_socket and self.running:
            try:
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                self.client_socket.send(message_header + message)
            except (OSError, BrokenPipeError):
                print("Disconnected from server.")
                self.running = False

    def receive_messages(self):
        """Handles receiving messages from the server."""
        username_header = self.client_socket.recv(HEADER_LENGTH)
        if not len(username_header):
            print("Connection closed by the server.")
            self.running = False
            return

        username_length = int(username_header.decode('utf-8'))
        username = self.client_socket.recv(username_length).decode('utf-8')

        message_header = self.client_socket.recv(HEADER_LENGTH)
        message_length = int(message_header.decode('utf-8'))
        message = self.client_socket.recv(message_length).decode('utf-8')

        print(f"{username} > {message}")
        self.received.emit(message)

    def stop(self):
        """Stops the thread and closes the connection."""
        self.running = False
        self.quit()
        self.wait()
