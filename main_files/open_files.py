
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QListWidgetItem, QMessageBox
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtCore import Qt, QUrl

class FileItemWidget(QWidget):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        file_name = os.path.basename(self.file_path)
        open_button = QPushButton(file_name)
        open_button.setIcon(QIcon("images/smile.svg"))  # You can set an icon if you want
        open_button.clicked.connect(self.open_file)

        layout.addWidget(open_button)

    def open_file(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(self.file_path))

class FileChat(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Chat")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        self.add_file_button = QPushButton("Add File")
        self.add_file_button.clicked.connect(self.add_file)
        layout.addWidget(self.add_file_button)

    def add_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")

        if file_path:
            file_item = QListWidgetItem(self.file_list)
            file_widget = FileItemWidget(file_path)
            file_item.setSizeHint(file_widget.sizeHint())
            self.file_list.addItem(file_item)
            self.file_list.setItemWidget(file_item, file_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat = FileChat()
    chat.show()
    sys.exit(app.exec())
