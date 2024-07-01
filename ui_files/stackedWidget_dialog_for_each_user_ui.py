# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stackedWidget_dialog_for_each_userNynpdt.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import resource_files.res_rc
from main_files.custom_QTextEdit import CustomQTextEdit


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(412, 111)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet("#widget {border-image: url(':tg_bg_img_2');}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 6, 6)
        self.listWidget_for_messages = QListWidget(self.widget)
        self.listWidget_for_messages.setObjectName(u"listWidget_for_messages")
        self.listWidget_for_messages.setMinimumSize(QSize(400, 0))
        self.listWidget_for_messages.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0);\n"
"border:none")
        self.listWidget_for_messages.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout.addWidget(self.listWidget_for_messages)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setStyleSheet(u"#widget_2 {\n"
"	background-color: rgb(80, 107, 157);\n"
"	border-radius: 5;\n"
"}\n"
"#btn_attach {\n"
"	border-image: url(':attach_img');\n"
"	border:none;\n"
"}\n"
"\n"
"#btn_attach:hover {\n"
"	border-image: url(':attach_hover');\n"
"	border:none;\n"
"}\n"
"\n"
"#btn_sticker {\n"
"	border-image: url(':sticker_img');\n"
"	border:none;\n"
"}\n"
"\n"
"#btn_sticker:hover {\n"
"	border-image: url(':sticker_hover');\n"
"	border:none;\n"
"}\n"
"\n"
"#btn_voice {\n"
"	border-image: url(':voice_img');\n"
"	border:none;\n"
"}\n"
"\n"
"#btn_voice:hover {\n"
"	border-image: url(':voice_hover');\n"
"	border:none;\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.btn_attach = QPushButton(self.widget_2)
        self.btn_attach.setObjectName(u"btn_attach")
        self.btn_attach.setMinimumSize(QSize(25, 25))
        self.btn_attach.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btn_attach)

        self.message_lineEdit = CustomQTextEdit(self.widget_2)
        self.message_lineEdit.setObjectName(u"message_lineEdit")
        sizePolicy1.setHeightForWidth(self.message_lineEdit.sizePolicy().hasHeightForWidth())
        self.message_lineEdit.setSizePolicy(sizePolicy1)
        self.message_lineEdit.setMinimumSize(QSize(0, 30))
        self.message_lineEdit.setMaximumSize(QSize(16777215, 150))
        self.message_lineEdit.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0); padding: 3")

        self.horizontalLayout_2.addWidget(self.message_lineEdit)

        self.btn_sticker = QPushButton(self.widget_2)
        self.btn_sticker.setObjectName(u"btn_sticker")
        self.btn_sticker.setMinimumSize(QSize(25, 25))
        self.btn_sticker.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btn_sticker)

        self.btn_voice = QPushButton(self.widget_2)
        self.btn_voice.setObjectName(u"btn_voice")
        self.btn_voice.setMinimumSize(QSize(25, 25))
        self.btn_voice.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btn_voice)

        self.btn_send_message = QPushButton(self.widget_2)
        self.btn_send_message.setObjectName(u"btn_send_message")
        self.btn_send_message.setMinimumSize(QSize(25, 25))
        self.btn_send_message.setMaximumSize(QSize(25, 25))
        self.btn_send_message.setStyleSheet(u"#btn_send_message {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"#btn_send_message:pressed {\n"
"	margin: 1 0 1 1;\n"
"}\n"
"\n"
"#btn_send_message:hover {\n"
"	border: 1 solid blue;\n"
"	border-radius: 5\n"
"}")
        icon = QIcon()
        icon.addFile(u":/send_img.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send_message.setIcon(icon)
        self.btn_send_message.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btn_send_message)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_attach.setText("")
        self.btn_sticker.setText("")
        self.btn_voice.setText("")
        self.btn_send_message.setText("")
    # retranslateUi

