from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import QWidget, QTextEdit

from ui_files.message_ui import Ui_Form


class Message(Ui_Form, QWidget):
    def __init__(self, align=None):
        super().__init__()
        self.setupUi(self)
        self.username_label.setStyleSheet('color:white')

        self.message_label = QTextEdit()
        self.message_label.setReadOnly(True)
        self.message_label.setStyleSheet('background-color: rgba(0, 0, 0, 0); color: white')
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
        metrics = QFontMetrics(self.message_label.font())
        text = self.message_label.toPlainText()
        lines = text.split('\n')
        max_width = max(metrics.horizontalAdvance(line) for line in lines)
        total_height = metrics.lineSpacing() * len(lines)
        if max_width > 500:
            max_width = 500
        # Adjust the size of the QTextEdit based on the content size
        print(max_width)
        print(total_height)
        self.message_label.setFixedSize(max_width + 20, total_height + 20)