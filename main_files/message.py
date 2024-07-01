from PySide6.QtCore import Qt
from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import QWidget, QTextEdit

from ui_files.message_ui import Ui_Form


class Message(Ui_Form, QWidget):
    def __init__(self, align=None):
        super().__init__()
        self.setupUi(self)
        self.username_label.setStyleSheet('color:white')

        self.message_label = QTextEdit()
        self.message_label.setLineWrapMode(QTextEdit.WidgetWidth)
        self.message_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.message_label.setMaximumWidth(400)
        self.message_label.setMaximumHeight(1400)
        self.message_label.setReadOnly(True)
        self.message_label.setStyleSheet('background-color: rgb(125, 166, 255); color: white; border-radius: 5;')
        if align == 'right':
            self.horizontalLayout.addStretch()
            self.horizontalLayout.addWidget(self.message_label)
        elif align == 'left':
            self.horizontalLayout.addWidget(self.message_label)
            self.horizontalLayout.addStretch()

    # def adjust_text_edit_size(self):
    #     document = self.message_label.document()
    #     document.setTextWidth(self.message_label.viewport().width())
    #     size = document.size()
    #
    #     text_width = size.width()
    #     text_height = size.height()
    #
    #     # Adjust the size of the QTextEdit based on the document size
    #     print(text_width)
    #     print(text_height)
    #     self.message_label.setFixedSize(text_width, text_height + 15)

    def adjust_text_edit_size(self):
        # metrics = QFontMetrics(self.message_label.font())
        # text = self.message_label.toPlainText()
        # lines = text.split('\n')
        # max_width = max(metrics.horizontalAdvance(line) for line in lines)
        # total_height = metrics.lineSpacing() * len(lines)
        #
        # # Adjust the size of the QTextEdit based on the content size
        # print(max_width)
        # print(total_height)
        # if max_width < 700:
        #     self.message_label.setFixedSize(max_width + 20, total_height + 20)

        doc_heigth = self.message_label.document().size().height()
        doc_width = self.message_label.document().size().width()
        if doc_heigth <= 1400 and doc_width <= 700:
            self.message_label.setFixedHeight(int(doc_heigth))
            self.message_label.setFixedWidth(int(doc_width))
        elif doc_heigth >= 1400 and doc_width >= 700:
            self.message_label.setFixedHeight(1400)
            self.message_label.setFixedWidth(700)
        else:
            self.message_label.setFixedHeight(1400)
            self.message_label.setFixedWidth(400)