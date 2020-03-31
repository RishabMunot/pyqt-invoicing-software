# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_page.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#data

data = {'rishab' : '1234','nainik':'1234'}
    

class Ui_Dialog(object):

    #function
    
    def login(self):
        username = self.username_edit.text()
        password =  self.password_edit.text()
        if(data.get(username) and data.get(username)==password):
            print("Login successful")
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Login failed")
            msg.setInformativeText('Incorrect Username/Password')
            msg.setWindowTitle("Error")
            msg.exec_()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(800, 650)
        
        font = QtGui.QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(240, 270, 331, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.username_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.username_edit.setEnabled(True)
        self.username_edit.setSizeIncrement(QtCore.QSize(10, 10))
        self.username_edit.setBaseSize(QtCore.QSize(0, 30))

        font = QtGui.QFont()
        font.setPointSize(9)
        self.username_edit.setFont(font)
        self.username_edit.setObjectName("username_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_edit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.password_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.password_edit.setFont(font)
        self.password_edit.setObjectName("password_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_edit)
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(370, 350, 93, 28))
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(380, 220, 131, 21))
        
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)

        self.login_button.clicked.connect(self.login)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Username :"))
        self.label_5.setText(_translate("Dialog", "Password :"))
        self.login_button.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
