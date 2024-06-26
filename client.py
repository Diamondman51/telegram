from random import choice, randint

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QRhiTexture
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QWidget, QListWidgetItem, QLabel

from client.tools.client_socket import ClientSocket
from client.ui.client_ui import Ui_clientForm

css = """
#message-blue {
    position: relative;
    margin-left: 20px;
    margin-bottom: 10px;
    padding: 10px;
    background-color: #A8DDFD;
    width: 200px;
    height: 50px;
    text-align: left;
    font: 400 .9em 'Open Sans', sans-serif;
    border: 1px solid #97C6E3;
    border-radius: 10px;
}

#message-blue:after {
    content: '';
    position: absolute;
    width: 0;
    height: 0;
    border-top: 15px solid #A8DDFD;
    border-left: 15px solid transparent;
    border-right: 15px solid transparent;
    top: 0;
    left: -15px;
}

#message-blue:before {
    content: '';
    position: absolute;
    width: 0;
    height: 0;
    border-top: 17px solid #97C6E3;
    border-left: 16px solid transparent;
    border-right: 16px solid transparent;
    top: -1px;
    left: -17px;
}
"""

class MessageWidget(QWidget):

    def __init__(self, message="", me=True, parent=None):
        super().__init__(parent)
        self.init_ui(me)
        self.setText(message)
        self.show()

    def init_ui(self, me):
        # Create a layout for the widget
        layout = QHBoxLayout()

        # Add a label and a button
        self.label = QLabel("Custom Item")
        if not me:
            self.label.setStyleSheet("background-color: rgba(0,255,0,0.3); padding: 5px;")
            self.label.setAlignment(Qt.AlignLeft)
        else:
            self.label.setStyleSheet("background-color: rgba(255,0,0,0.3); padding: 5px;")
            self.label.setAlignment(Qt.AlignRight)
        self.setStyleSheet(css)
        self.label.setObjectName('message-blue')
        # Add widgets to the layout
        layout.addWidget(self.label)

        # Set layout to the custom widget
        self.setLayout(layout)

    def setText(self, text):
        self.label.setText(text)

    def getText(self):
        return self.label.text()


class Client(QWidget, Ui_clientForm):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.edit_text.setFocus()
        self.setBaseSize(QSize(500, 1000))
        self.btn_send.clicked.connect(self.on_btn_send_clicked)
        self.setWindowTitle("Gap")

        username = choice(["Otabek", "Jasur", "Anvar", "Bekzod", "Sherzod"]) + f'_{randint(1000, 2000)}'

        self.client_socket = ClientSocket(username)
        self.client_socket.received.connect(self.on_message_received)
        self.client_socket.connected.connect(lambda: self.set_internet_sign())
        self.client_socket.disconnected.connect(lambda: self.set_internet_sign(False))

        self.client_socket.start()

    def set_internet_sign(self, on=True):
        self.lbl_internet.setPixmap(QPixmap(f":/images/images/wifi_{'on' if on else 'off'}.png"))

    def on_message_received(self, message):
        self.append_message(message, False)

    def on_btn_send_clicked(self):
        text = self.edit_text.text().strip()
        self.append_message(text)
        self.client_socket.send_message(text)

    def append_message(self, text, me=True):
        item = QListWidgetItem()
        self.listWidget.addItem(item)
        widget = MessageWidget(text, me, self.listWidget)
        item.setSizeHint(widget.sizeHint())
        self.listWidget.setItemWidget(item, widget)

