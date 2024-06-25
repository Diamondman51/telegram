# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messageixUbtt.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(122, 84)
        Form.setStyleSheet(u"padding: 5")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.username_label = QLabel(Form)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(14)
        self.username_label.setFont(font)

        self.verticalLayout.addWidget(self.username_label)

        self.message_label = QLabel(Form)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.message_label.setFont(font1)

        self.verticalLayout.addWidget(self.message_label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.username_label.setText(QCoreApplication.translate("Form", u"Username", None))
        self.message_label.setText(QCoreApplication.translate("Form", u"Message text", None))
    # retranslateUi

