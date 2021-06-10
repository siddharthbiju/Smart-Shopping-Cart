

import sys
import platform
from PyQt5.uic import loadUi
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


try:
    cred = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db=firestore.client()


from ui_main import Ui_MainWindow
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_page_2.setEnabled(False)
        self.ui.btn_page_3.setEnabled(False)
        self.ui.btn_page_4.setEnabled(False)
        self.ui.btn_page_5.setEnabled(False)
        self.ui.label_5.setText("Invalid User!!")
        self.ui.label_5.setVisible(False)
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 300)
        self.ui.tableWidget.setColumnWidth(2, 200)
        self.ui.tableWidget.setColumnWidth(3, 100)
        

        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))

        self.show()

        self.ui.pushButton_5.clicked.connect(self.login)
        self.ui.pushButton_6.clicked.connect(self.Ins)
        self.ui.pushButton.clicked.connect(self.view)
        self.ui.pushButton_7.clicked.connect(self.Del)
        self.ui.pushButton_8.clicked.connect(self.Upd)
        self.ui.label_25.setVisible(False)
        self.ui.label_34.setVisible(False)

        self.ui.lineEdit_26.setVisible(False)
        self.ui.lineEdit_30.setVisible(False)



        if self.ui.checkBox.isChecked()==True:
            self.ui.label_32.setVisible(True)
            self.ui.lineEdit_29.setVisible(True)
        if self.ui.checkBox_2.isChecked()==True:
            self.ui.label_33.setVisible(True)
            self.ui.lineEdit_24.setVisible(True)
        if self.ui.checkBox_3.isChecked()==True:
            self.ui.label_31.setVisible(True)
            self.ui.lineEdit_31.setVisible(True)

    def login(self):
        id1=self.ui.lineEdit.text()
        password=self.ui.lineEdit_2.text()
        print(id1)
        print(password)
        logi = db.collection('users').document('Emp1321123asxcp').get()
        x = logi.to_dict()
        if id1 == x['Id'] and x['password'] == password:
            print("Successfully logged in with id: ", id1, "and password:", password)
            self.ui.label_5.setStyleSheet('color: lightgreen')
            self.ui.label_5.setText("Access granted!!")
            self.ui.btn_page_2.setEnabled(True)
            self.ui.btn_page_3.setEnabled(True)
            self.ui.btn_page_4.setEnabled(True)
            self.ui.btn_page_5.setEnabled(True)
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        else:
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.label_5.setVisible(True)

    def Ins(self):
        iid = self.ui.lineEdit_26.text()
        iname = self.ui.lineEdit_27.text()
        rval = self.ui.lineEdit_23.text()
        price = self.ui.lineEdit_25.text()
        data = {'Name': iname,
                'RFID value': rval,
                'Price': price}
        db.collection('Items').document(rval).set(data)
        self.ui.lineEdit_26.clear()
        self.ui.lineEdit_27.clear()
        self.ui.lineEdit_23.clear()
        self.ui.lineEdit_25.clear()

    def view(self):
        row=0
        vdata = db.collection('Items').get()
        print(len(vdata))
        print(vdata)
        self.ui.tableWidget.setRowCount(len(vdata))
        for vvdata in vdata:
            y=vvdata.to_dict()
            print(y)
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(y['Name']))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(y['RFID value']))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(y['Price']))
            row=row+1

    def Del(self):
        diid=self.ui.lineEdit_28.text()
        res=db.collection('Items').document(diid).get()
        if res.exists:
            db.collection('Items').document(diid).delete()
            self.ui.label_7.setText('Status : Deleted Succesfully')
        else:
            self.ui.label_7.setText('Status : No such data exists')
            print('No such data exists')
        self.ui.lineEdit_28.clear()

    def Upd(self):
        Uid=self.ui.lineEdit_30.text()
        nprice = self.ui.lineEdit_31.text()
        nrval = self.ui.lineEdit_24.text()
        nname = self.ui.lineEdit_29.text()

        if self.ui.checkBox.isChecked():
             db.collection('Items').document(nrval).update({'Name' : nname})
             self.ui.label_8.setText('Status : Updated name')
        if self.ui.checkBox_3.isChecked():
            db.collection('Items').document(nrval).update({'Price': nprice})
            self.ui.label_8.setText('Status : Updated price')
        else:
            self.ui.label_8.setText('Status : No value selected')
        
        self.ui.lineEdit_31.clear()
        self.ui.lineEdit_24.clear()
        self.ui.lineEdit_29.clear()
        self.ui.lineEdit_30.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
