from PySide6.QtCore import QSize
from PySide6.QtWidgets import QTextEdit


class CustomQTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__()
        self.setPlaceholderText('Enter text...')
        self.textChanged.connect(self.new_size)

    def new_size(self):
        # doc = self.document()
        # docSize = doc.size()
        # newHeight = int(docSize.height()) + self.frameWidth() * 2
        # if newHeight <= 150:
        #     self.setFixedHeight(newHeight)

        doc_height = self.document().size().height()
        if 30 <= doc_height <= 150:
            self.setFixedHeight(int(doc_height))
        elif doc_height <= 29:
            self.setFixedHeight(30)
        else:
            self.setFixedHeight(150)
