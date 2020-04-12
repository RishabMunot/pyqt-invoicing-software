# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functions_dashboard import f_addVendor,f_addProduct

class Ui_MainWindow(object):
    

    def addVendor(self):
        f_addVendor(self)
    def addProduct(self):
        f_addProduct(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 530)
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
        self.label.setGeometry(QtCore.QRect(350, 170, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.add_product = QtWidgets.QPushButton(self.centralwidget)
        self.add_product.setGeometry(QtCore.QRect(280, 270, 231, 41))
        self.add_product.setObjectName("add_product")
        self.add_vendor = QtWidgets.QPushButton(self.centralwidget)
        self.add_vendor.setGeometry(QtCore.QRect(280, 220, 231, 41))
        self.add_vendor.setObjectName("add_vendor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.add_vendor.clicked.connect(self.addVendor)
        self.add_product.clicked.connect(self.addProduct)  

        self.retranslateUi(MainWindow)
        self.add_vendor.clicked['bool'].connect(MainWindow.setAnimated)
        self.add_product.clicked['bool'].connect(MainWindow.setAnimated)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dashboard"))
        self.add_product.setText(_translate("MainWindow", "Add Product"))
        self.add_vendor.setText(_translate("MainWindow", "Add Vendor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
