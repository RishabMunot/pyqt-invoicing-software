# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from add_new_product import Ui_window_anp
from add_new_vendor import Ui_window_anv
from window_bill import Ui_window_bill


class Ui_MainWindow(object):
   
   
        #functionsQtWidgets.QMainWindow()
    def createNewBill(self):
        self.window_anp = QtWidgets.QMainWindow()
        self.ui = Ui_window_bill()
        self.ui.setupUi(self.window_anp)
        self.window_anp.show()

    def editBill(self):
        self.window_anp = QtWidgets.QMainWindow()
        self.ui = Ui_window_bill()
        self.ui.setupUi(self.window_anp)
        self.window_anp.show()
    
    def addVendor(self):
        self.window_anp = QtWidgets.QMainWindow()
        self.ui = Ui_window_anv()
        self.ui.setupUi(self.window_anp)
        self.window_anp.show()
    def addProduct(self):
        self.window_anp = QtWidgets.QDialog()
        self.ui = Ui_window_anp()
        self.ui.setupUi(self.window_anp)
        self.window_anp.show()
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 180, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.create_new_bill = QtWidgets.QPushButton(self.centralwidget)
        self.create_new_bill.setGeometry(QtCore.QRect(280, 230, 231, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_new_bill.sizePolicy().hasHeightForWidth())
        self.create_new_bill.setSizePolicy(sizePolicy)
        self.create_new_bill.setObjectName("create_new_bill")
        self.add_product = QtWidgets.QPushButton(self.centralwidget)
        self.add_product.setGeometry(QtCore.QRect(280, 380, 231, 41))
        self.add_product.setObjectName("add_product")
        self.add_vendor = QtWidgets.QPushButton(self.centralwidget)
        self.add_vendor.setGeometry(QtCore.QRect(280, 330, 231, 41))
        self.add_vendor.setObjectName("add_vendor")
        self.edit_bill = QtWidgets.QPushButton(self.centralwidget)
        self.edit_bill.setGeometry(QtCore.QRect(280, 280, 231, 41))
        self.edit_bill.setObjectName("edit_bill")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        self.create_new_bill.clicked.connect(self.createNewBill)
        self.edit_bill.clicked.connect(self.editBill)
        self.add_vendor.clicked.connect(self.addVendor)
        self.add_product.clicked.connect(self.addProduct)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dashboard"))
        self.create_new_bill.setText(_translate("MainWindow", "Create new Bill"))
        self.add_product.setText(_translate("MainWindow", "Add Product"))
        self.add_vendor.setText(_translate("MainWindow", "Add Vendor"))
        self.edit_bill.setText(_translate("MainWindow", "Edit Bill"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
