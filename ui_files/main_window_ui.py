# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windownCkmLb.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_files.res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(979, 600)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"#page {\n"
"border-image: url(':tg_bg_img_2');\n"
"background-repeat:no-repeat;\n"
"background-position: center;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 6, 10)
        self.listWidget_for_messages = QListWidget(self.page)
        self.listWidget_for_messages.setObjectName(u"listWidget_for_messages")
        self.listWidget_for_messages.setMinimumSize(QSize(400, 0))
        self.listWidget_for_messages.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);\n"
"border:none")
        self.listWidget_for_messages.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_2.addWidget(self.listWidget_for_messages)

        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 5;")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 15, 0)
        self.message_lineEdit = QLineEdit(self.widget_3)
        self.message_lineEdit.setObjectName(u"message_lineEdit")
        self.message_lineEdit.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(12)
        self.message_lineEdit.setFont(font)
        self.message_lineEdit.setStyleSheet(u"padding:  0 0 0 5;")

        self.horizontalLayout.addWidget(self.message_lineEdit)

        self.btn_send_message = QPushButton(self.widget_3)
        self.btn_send_message.setObjectName(u"btn_send_message")
        self.btn_send_message.setMinimumSize(QSize(50, 22))
        self.btn_send_message.setStyleSheet(u"#btn_send_message:pressed {\n"
"	margin: 1 0 0 1\n"
"}\n"
"\n"
"#btn_send_message:hover {\n"
"	border: 1 solid rgb(105, 183, 255);\n"
"	border-radius: 5;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_send_message)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 3, 1, 2)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(166, 0))
        self.widget_2.setMaximumSize(QSize(220, 16777215))
        self.widget_2.setStyleSheet(u"background-color: rgb(71, 99, 150);\n"
"")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 541, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.username_LineEdit = QLineEdit(self.widget_2)
        self.username_LineEdit.setObjectName(u"username_LineEdit")
        self.username_LineEdit.setStyleSheet(u"padding: 0 0 2 5;\n"
"color: white;\n"
"border:none;")

        self.gridLayout.addWidget(self.username_LineEdit, 1, 1, 1, 1)

        self.btn_menu_2 = QPushButton(self.widget_2)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        self.btn_menu_2.setMinimumSize(QSize(50, 45))
        self.btn_menu_2.setMaximumSize(QSize(50, 40))
        self.btn_menu_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_2.setIcon(icon)
        self.btn_menu_2.setIconSize(QSize(32, 32))
        self.btn_menu_2.setCheckable(True)
        self.btn_menu_2.setAutoExclusive(True)
        self.btn_menu_2.setAutoRepeatDelay(300)
        self.btn_menu_2.setAutoRepeatInterval(100)

        self.gridLayout.addWidget(self.btn_menu_2, 0, 0, 2, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 3, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(65, 16777215))
        self.widget.setStyleSheet(u"background-color: rgb(71, 99, 150);\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_menu_1 = QPushButton(self.widget)
        self.btn_menu_1.setObjectName(u"btn_menu_1")
        self.btn_menu_1.setMinimumSize(QSize(50, 45))
        self.btn_menu_1.setMaximumSize(QSize(50, 40))
        self.btn_menu_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_menu_1.setIcon(icon)
        self.btn_menu_1.setIconSize(QSize(32, 32))
        self.btn_menu_1.setCheckable(True)
        self.btn_menu_1.setChecked(False)
        self.btn_menu_1.setAutoRepeat(False)
        self.btn_menu_1.setAutoExclusive(True)
        self.btn_menu_1.setAutoRepeatDelay(300)
        self.btn_menu_1.setAutoRepeatInterval(100)

        self.verticalLayout.addWidget(self.btn_menu_1)

        self.verticalSpacer = QSpacerItem(20, 541, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 3, 1)

        self.users_listWidget = QListWidget(Form)
        self.users_listWidget.setObjectName(u"users_listWidget")
        self.users_listWidget.setMinimumSize(QSize(300, 0))
        self.users_listWidget.setMaximumSize(QSize(320, 16777215))

        self.gridLayout_2.addWidget(self.users_listWidget, 0, 2, 1, 1)


        self.retranslateUi(Form)
        self.btn_menu_1.clicked["bool"].connect(self.widget_2.setVisible)
        self.btn_menu_2.toggled.connect(self.widget.setVisible)
        self.btn_menu_2.toggled.connect(self.widget_2.setHidden)
        self.btn_menu_1.toggled.connect(self.widget.setHidden)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.message_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter messsage...", None))
        self.btn_send_message.setText(QCoreApplication.translate("Form", u"Send", None))
        self.username_LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"username", None))
        self.btn_menu_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Username", None))
    # retranslateUi

