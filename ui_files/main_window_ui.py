# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowyiaqOo.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_files.res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(979, 635)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        icon = QIcon()
        icon.addFile(u":/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_1.setIcon(icon)
        self.btn_menu_1.setIconSize(QSize(32, 32))
        self.btn_menu_1.setCheckable(True)
        self.btn_menu_1.setChecked(False)
        self.btn_menu_1.setAutoRepeat(False)
        self.btn_menu_1.setAutoExclusive(True)
        self.btn_menu_1.setAutoRepeatDelay(1000)
        self.btn_menu_1.setAutoRepeatInterval(50)

        self.verticalLayout.addWidget(self.btn_menu_1)

        self.verticalSpacer = QSpacerItem(20, 541, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(166, 0))
        self.widget_2.setMaximumSize(QSize(220, 16777215))
        self.widget_2.setStyleSheet(u"background-color: rgb(71, 99, 150);\n"
"")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 541, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.btn_menu_2 = QPushButton(self.widget_2)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        self.btn_menu_2.setMinimumSize(QSize(50, 45))
        self.btn_menu_2.setMaximumSize(QSize(50, 40))
        self.btn_menu_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn_menu_2.setIcon(icon)
        self.btn_menu_2.setIconSize(QSize(32, 32))
        self.btn_menu_2.setCheckable(True)
        self.btn_menu_2.setAutoRepeat(False)
        self.btn_menu_2.setAutoExclusive(True)
        self.btn_menu_2.setAutoRepeatDelay(1000)
        self.btn_menu_2.setAutoRepeatInterval(50)

        self.gridLayout.addWidget(self.btn_menu_2, 0, 0, 2, 1)

        self.username_LineEdit = QLineEdit(self.widget_2)
        self.username_LineEdit.setObjectName(u"username_LineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username_LineEdit.sizePolicy().hasHeightForWidth())
        self.username_LineEdit.setSizePolicy(sizePolicy1)
        self.username_LineEdit.setStyleSheet(u"padding: 0 0 2 5;\n"
"color: white;\n"
"border:none;")

        self.gridLayout.addWidget(self.username_LineEdit, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 0, 1, 1, 1)

        self.users_listWidget = QListWidget(Form)
        self.users_listWidget.setObjectName(u"users_listWidget")
        self.users_listWidget.setMinimumSize(QSize(300, 0))
        self.users_listWidget.setMaximumSize(QSize(320, 16777215))
        self.users_listWidget.setStyleSheet(u"alternate-background-color: rgb(129, 196, 255);\n"
"background-color: rgb(71, 99, 150);\n"
"")
        self.users_listWidget.setAlternatingRowColors(True)

        self.gridLayout_3.addWidget(self.users_listWidget, 0, 2, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 3, 1, 1)


        self.retranslateUi(Form)
        self.btn_menu_1.clicked["bool"].connect(self.widget.setHidden)
        self.btn_menu_1.clicked["bool"].connect(self.widget_2.setVisible)
        self.btn_menu_2.clicked["bool"].connect(self.widget.setVisible)
        self.btn_menu_2.clicked["bool"].connect(self.widget_2.setHidden)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username", None))
        self.btn_menu_2.setText("")
        self.username_LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"username", None))
    # retranslateUi

