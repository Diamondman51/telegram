from PySide6.QtWidgets import QApplication

from Login_page import Login_page
from main_files.main_window import Main_Window

app = QApplication()

# login = Login_page()
# login.show()

main_window = Main_Window()
main_window.show()

app.exec()