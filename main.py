from PySide6.QtWidgets import QApplication

from main_files.Login_page import Login_page
from main_files.main_window import Main_Window

app = QApplication()

login = Login_page()
res = login.exec()
if res == Login_page.Accepted:
    main_window = Main_Window()
    main_window.username_LineEdit.setText(login.text)
    main_window.username_LineEdit.setReadOnly(True)
    main_window.send_message_login(main_window.username_LineEdit.text(), 'entered to the group')
    # main_window.add_to_users(login.text)
    main_window.show()
app.exec()

