# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_bill.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_bill(object):
    def setupUi(self, window_bill):
        window_bill.setObjectName("window_bill")
        window_bill.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(window_bill)
        self.centralwidget.setObjectName("centralwidget")
        window_bill.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(window_bill)
        self.statusbar.setObjectName("statusbar")
        window_bill.setStatusBar(self.statusbar)

        self.retranslateUi(window_bill)
        QtCore.QMetaObject.connectSlotsByName(window_bill)

    def retranslateUi(self, window_bill):
        _translate = QtCore.QCoreApplication.translate
        window_bill.setWindowTitle(_translate("window_bill", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_bill = QtWidgets.QMainWindow()
    ui = Ui_window_bill()
    ui.setupUi(window_bill)
    window_bill.show()
    sys.exit(app.exec_())
