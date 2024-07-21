from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QGridLayout, QScrollArea, QVBoxLayout, QToolButton, QDialog

from ui_files.stackedWidget_dialog_for_each_user_ui import Ui_Form


class Dialog_for_each_user(Ui_Form, QWidget):

    sticker = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.create_sticker_widget()
        self.btn_sticker.clicked.connect(self.create_sticker_widget)

    def create_sticker_widget(self):
        sticks = '😀😁😂🤣😃😄😎😋😊😉😆😅😍😘😗🥰😙🥲🤔🤩🤗🙂☺️😚🫡🤨😐😑😶🫥😮😥😣😏🙄😶‍🌫️🤐😯😪😫🥱😴😒🤤😝😜😛😌😓😔😕🫤🙃🫠😞😖🙁☹️😲🤑😟😤😢😭😦😧😰😮‍💨😬🤯😩😨😱🥵😳🤪😵😷🤬😡😠🥴😵‍💫🤒🤕🤢🤮🤧😇🤡🤠🥹🥺🥸🥳🤥🫨🙂‍↔️🙂‍↕️🤫🤭👿😈🧐🤓🫣🫢👹👺💀☠️👻👽😹😸😺💩🤖👾😻😼😽🙀😿😾🐺🐶🐵🙊🙉🙈🐱🦁🦒🐯🦊🦝🐰🐹🐭'
        dict_ = {}
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle('Stickers')
        self.dialog.setWindowIcon(QIcon("images/smile.svg"))
        self.vbox = QVBoxLayout(self.dialog)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.grid = QGridLayout(self.scroll_area_widget)
        path = [(i, j) for i in range(len(sticks)//9) for j in range(9)]
        for stick, destination in zip(sticks, path):
            dict_[stick] = QToolButton(self.scroll_area_widget)
            dict_[stick].setFixedSize(40, 40)
            dict_[stick].setText(stick)
            dict_[stick].clicked.connect(self.add_sticker)
            self.grid.addWidget(dict_[stick], *destination)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.grid.setSpacing(0)
        self.scroll_area_widget.setContentsMargins(0, 0, 0, 0)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.vbox.addWidget(self.scroll_area)
        self.dialog.setFixedWidth(self.grid.sizeHint().width()+50)
        self.dialog.show()
        self.message_lineEdit.setFocus()

    def add_sticker(self):
        cursor = self.message_lineEdit.textCursor()
        sticker = self.sender().text()
        cursor.insertText(sticker)
        # text = self.message_lineEdit.toPlainText()
        self.message_lineEdit.setTextCursor(cursor)

    # TODO ChatGPT

    # def insert_sticker(self, sticker):
    #     cursor = self.message_text_edit.textCursor()
    #     cursor.insertText(sticker)
    #     self.message_text_edit.setTextCursor(cursor)
