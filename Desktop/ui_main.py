# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainEUItbX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1012, 620)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_left_menu)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_left_menu)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_left_menu)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_3)

        self.btn_page_4 = QPushButton(self.frame_left_menu)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_4)

        self.btn_page_5 = QPushButton(self.frame_left_menu)
        self.btn_page_5.setObjectName(u"btn_page_5")
        self.btn_page_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_5)

        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(430, 200, 161, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(430, 400, 151, 51))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(103, 103, 103);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 210, 101, 21))
        self.label_3.setStyleSheet(u"color: rgb(7, 200, 222);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 280, 121, 21))
        self.label_4.setStyleSheet(u"color: rgb(7, 200, 222);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 350, 131, 21))
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(430, 280, 161, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(430, 80, 151, 41))
        self.label_6.setStyleSheet(u"color: rgb(226, 226, 226);\n"
"font: 28pt \"MS Shell Dlg 2\";")

        self.verticalLayout_7.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(280, 200, 71, 21))
        self.label_25.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_27 = QLineEdit(self.frame_2)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(380, 250, 221, 31))
        self.lineEdit_27.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_25 = QLineEdit(self.frame_2)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setGeometry(QRect(380, 350, 221, 31))
        self.lineEdit_25.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(420, 440, 141, 41))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 170, 255);")
        self.lineEdit_26 = QLineEdit(self.frame_2)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(380, 190, 221, 31))
        self.lineEdit_26.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_23 = QLineEdit(self.frame_2)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setGeometry(QRect(380, 301, 221, 31))
        self.lineEdit_23.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(180, 300, 141, 21))
        self.label_29.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_26 = QLabel(self.frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(250, 350, 71, 21))
        self.label_26.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(240, 250, 71, 21))
        self.label_30.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(430, 40, 441, 71))
        self.label_27.setStyleSheet(u"font: 28pt \"MS Shell Dlg 2\";\n"
"color: rgb(227, 227, 227);")

        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 891, 381))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 450, 141, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(103, 103, 103);")

        self.verticalLayout_8.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.frame_5 = QFrame(self.page_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 911, 661))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 30, 251, 101))
        self.label_2.setStyleSheet(u"color: rgb(226, 226, 226);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(190, 320, 71, 21))
        self.label_31.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_24 = QLineEdit(self.frame_5)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setGeometry(QRect(320, 271, 221, 31))
        self.lineEdit_24.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_32 = QLabel(self.frame_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(180, 220, 71, 21))
        self.label_32.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_29 = QLineEdit(self.frame_5)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(QRect(320, 220, 221, 31))
        self.lineEdit_29.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_30 = QLineEdit(self.frame_5)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(QRect(320, 160, 221, 31))
        self.lineEdit_30.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_33 = QLabel(self.frame_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(120, 270, 141, 21))
        self.label_33.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(360, 410, 141, 41))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 170, 255);")
        self.lineEdit_31 = QLineEdit(self.frame_5)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setGeometry(QRect(320, 320, 221, 31))
        self.lineEdit_31.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_34 = QLabel(self.frame_5)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(220, 170, 71, 21))
        self.label_34.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(350, 370, 251, 21))
        self.label_8.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 255, 0);")
        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(650, 230, 111, 21))
        self.checkBox.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.checkBox_2 = QCheckBox(self.frame_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(650, 280, 121, 21))
        self.checkBox_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.checkBox_3 = QCheckBox(self.frame_5)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(650, 330, 121, 21))
        self.checkBox_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.frame_3 = QFrame(self.page_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 10, 981, 561))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lineEdit_28 = QLineEdit(self.frame_3)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(330, 210, 221, 31))
        self.lineEdit_28.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(360, 320, 141, 41))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 170, 255);")
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(250, 210, 71, 21))
        self.label_28.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 50, 221, 71))
        self.label.setStyleSheet(u"color: rgb(226, 226, 226);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(370, 270, 301, 21))
        self.label_7.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 255, 0);")
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_page_5.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Invalid User!!!", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"RFID Value", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"RFID Value", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"RFID Value", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Status : ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"RFID Value", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"RFID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Status : ", None))
    # retranslateUi

