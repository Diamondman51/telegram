# # import os
# # import sys
# # from PySide6.QtCore import *
# # from PySide6.QtGui import *
# # from PySide6.QtWidgets import *
# #
# #
# # class MainWindow(QWidget):
# #     def __init__(self):
# #         super(MainWindow, self).__init__()
# #
# #         self.lay = QHBoxLayout()
# #         self.sidebar = QWidget()
# #         self.sidebar_layout = QHBoxLayout()
# #         self.button_container = QWidget()
# #         self.b1 = QPushButton("Button1")
# #         self.b2 = QPushButton("Button2")
# #         self.button_container_layout = QVBoxLayout()
# #
# #         self.popup = QWidget()
# #
# #         self.anim_popup = QPropertyAnimation(self.popup, b"geometry")
# #
# #         self.InitUI()
# #
# #     def InitUI(self):
# #         self.resize(500, 400)
# #
# #         self.button_container.installEventFilter(self)
# #
# #         self.popup.setStyleSheet("background: red;")
# #         self.popup.setGeometry(-100, -100, 0, 0)
# #         self.popup.setParent(self)
# #
# #         self.button_container_layout.addWidget(self.b1)
# #         self.button_container_layout.addWidget(self.b2)
# #         self.button_container.setStyleSheet("background: rgb(80, 80, 80);")
# #         self.button_container.setFixedHeight(100)
# #         self.button_container.setMouseTracking(True)
# #         self.button_container.setLayout(self.button_container_layout)
# #
# #         self.sidebar_layout.addWidget(self.button_container)
# #         self.sidebar.setFixedWidth(100)
# #         self.sidebar.setMouseTracking(True)
# #         self.sidebar.setStyleSheet("background: rgb(40, 40, 40);")
# #         self.sidebar.setLayout(self.sidebar_layout)
# #         self.lay.addWidget(self.sidebar)
# #         self.lay.setAlignment(self.sidebar, Qt.AlignLeft)
# #         self.setLayout(self.lay)
# #
# #     def AnimPopup(self):
# #         self.anim_popup.setStartValue(QRect(-100, -100, 0, 0))
# #         self.anim_popup.setEndValue(QRect(100, 200, 100, 100))
# #         self.anim_popup.setDuration(1000)
# #         self.anim_popup.start()
# #
# #     def eventFilter(self, obj, ev):
# #         if ev.type() == QEvent.Enter:
# #             print("Entered")
# #             self.AnimPopup()
# #
# #         return False
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     mw = MainWindow()
# #     mw.show()
# #     sys.exit(app.exec_())
# #
#
#
# #
# # import sys
# # from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu
# #
# #
# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #
# #         # Set up the main window
# #         self.setWindowTitle("Resize QMenu Example")
# #         self.setGeometry(100, 100, 300, 200)
# #
# #         # Create a QPushButton
# #         self.button = QPushButton("Open Menu", self)
# #         self.button.setGeometry(100, 80, 100, 40)
# #
# #         # Create a QMenu
# #         self.menu = QMenu(self)
# #
# #         # Add actions to the menu
# #         self.menu.addAction("Option 1")
# #         self.menu.addAction("Option 2")
# #         self.menu.addAction("Option 3")
# #
# #         # Apply stylesheets for resizing the menu
# #         self.menu.setStyleSheet("""
# #             QMenu {
# #                 min-width: 550px; /* Minimum width of the menu */
# #                 max-width: 150px; /* Maximum width of the menu */
# #                 background-color: white;
# #                 border: 1px solid black;
# #             }
# #             QMenu::item {
# #                 padding: 10px 20px; /* Adjust padding for menu items */
# #             }
# #         """)
# #
# #         # Connect the button to show the menu
# #         self.button.setMenu(self.menu)
# #         self.button.clicked.connect(lambda: self.button.setVisible(False))
# #
# #
# # # Create the application instance
# # app = QApplication(sys.argv)
# #
# # # Create the main window instance
# # window = MainWindow()
# # window.show()
# #
# # # Execute the application
# # sys.exit(app.exec())
#
#
# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu
#
#
# class CustomMenu(QMenu):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#     def sizeHint(self):
#         size = super().sizeHint()
#         size.setWidth(200)  # Set your desired width
#         size.setHeight(size.height())  # Optionally set a desired height
#         return size
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Set up the main window
#         self.setWindowTitle("Resize QMenu Example")
#         self.setGeometry(100, 100, 300, 200)
#
#         # Create a QPushButton
#         self.button = QPushButton("Open Menu", self)
#         self.button.setGeometry(100, 80, 100, 40)
#
#         # Create a CustomMenu
#         self.menu = CustomMenu(self)
#
#         # Add actions to the menu
#         self.menu.addAction("Option 1")
#         self.menu.addAction("Option 2")
#         self.menu.addAction("Option 3")
#
#         # Connect the button to show the menu
#         self.button.setMenu(self.menu)
#
#
# # Create the application instance
# app = QApplication(sys.argv)
#
# # Create the main window instance
# window = MainWindow()
# window.show()
#
# # Execute the application
# sys.exit(app.exec())


import socket
import sys
import threading
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

def send_messages(client_socket):
    """Handles sending messages to the server."""
    while True:
        try:
            message = input(f"")
            if message:
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                client_socket.send(message_header + message)
        except (OSError, BrokenPipeError):
            print("Disconnected from server.")
            break

def receive_messages(client_socket):
    """Handles receiving messages from the server."""
    while True:
        try:
            while True:
                username_header = client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print("Connection closed by the server.")
                    sys.exit()

                username_length = int(username_header.decode('utf-8'))
                username = client_socket.recv(username_length).decode('utf-8')

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8'))
                message = client_socket.recv(message_length).decode('utf-8')

                print(f"{username} > {message}")

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print("Reading error", e)
                sys.exit()
            continue

        except Exception as e:
            print('General error', e)
            sys.exit()


my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(True)

# Serverga foydalanuvchi ismini yuborish
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

# yuboruvchi va qabul qiluvchi oqimlarni yaratish
send_thread = threading.Thread(target=send_messages, args=(client_socket,))
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))

# yuboruvchi va qabul qiluvchi oqimlarni ishga tushirish
send_thread.start()
receive_thread.start()

# asosiy oqim (thread) bu oqimlarni kutib turadi
send_thread.join()
receive_thread.join()

client_socket.close()