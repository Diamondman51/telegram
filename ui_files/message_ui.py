# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messageIHCzqX.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(245, 72)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
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

        self.widgett = QWidget(Form)
        self.widgett.setObjectName(u"widgett")
        sizePolicy.setHeightForWidth(self.widgett.sizePolicy().hasHeightForWidth())
        self.widgett.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widgett)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.widgett)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.username_label.setText(QCoreApplication.translate("Form", u"Username", None))
    # retranslateUi

