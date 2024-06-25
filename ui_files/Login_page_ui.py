# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_pageqKgSKj.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_files.res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(886, 587)
        Dialog.setMinimumSize(QSize(886, 587))
        Dialog.setMaximumSize(QSize(886, 587))
        Dialog.setStyleSheet(u"QDialog {\n"
"	border-image: url(':images/bg_img2');\n"
"	background-size: cover;\n"
"\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(600, 500))
        self.stackedWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 200))
        self.frame.setStyleSheet(u"QFrame {\n"
"	color:white;\n"
"	background-color: rgba(171, 255, 234, 0.3);\n"
"	border-radius: 10;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(126, 175, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	margin: 1 0 0 1\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.label)

        self.user_name_lineEdit = QLineEdit(self.frame)
        self.user_name_lineEdit.setObjectName(u"user_name_lineEdit")
        self.user_name_lineEdit.setMinimumSize(QSize(0, 30))
        self.user_name_lineEdit.setMaximumSize(QSize(16777215, 78))
        self.user_name_lineEdit.setStyleSheet(u"color:black;\n"
"margin: 20 0 20 0;\n"
"border-radius: 5;\n"
"padding: 5;\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.user_name_lineEdit)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.btn_login.setFont(font2)
        self.btn_login.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.btn_login)

        self.btn_signup = QPushButton(self.frame)
        self.btn_signup.setObjectName(u"btn_signup")
        self.btn_signup.setMinimumSize(QSize(0, 30))
        self.btn_signup.setFont(font2)
        self.btn_signup.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.btn_signup)


        self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 238))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	color:white;\n"
"	background-color: rgba(171, 255, 234, 0.3);\n"
"	border-radius: 10;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: black;\n"
"	border-radius: 5;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color:  rgba(126, 175, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	margin: 1 0 0 1;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 45))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.user_name_lineEdit_sign_up_page = QLineEdit(self.frame_2)
        self.user_name_lineEdit_sign_up_page.setObjectName(u"user_name_lineEdit_sign_up_page")
        self.user_name_lineEdit_sign_up_page.setMinimumSize(QSize(0, 30))
        self.user_name_lineEdit_sign_up_page.setMaximumSize(QSize(16777215, 78))
        self.user_name_lineEdit_sign_up_page.setStyleSheet(u"color:black;\n"
"margin: 20 0 20 0;\n"
"border-radius: 5;\n"
"padding: 5;\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.user_name_lineEdit_sign_up_page)

        self.btn_signup_sign_up_page = QPushButton(self.frame_2)
        self.btn_signup_sign_up_page.setObjectName(u"btn_signup_sign_up_page")
        self.btn_signup_sign_up_page.setMinimumSize(QSize(0, 30))
        self.btn_signup_sign_up_page.setFont(font2)
        self.btn_signup_sign_up_page.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_signup_sign_up_page)


        self.gridLayout_3.addWidget(self.frame_2, 1, 1, 2, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Login Page", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.user_name_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"put username", None))
        self.btn_login.setText(QCoreApplication.translate("Dialog", u"Log in", None))
        self.btn_signup.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.user_name_lineEdit_sign_up_page.setPlaceholderText(QCoreApplication.translate("Dialog", u"put username", None))
        self.btn_signup_sign_up_page.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
    # retranslateUi

