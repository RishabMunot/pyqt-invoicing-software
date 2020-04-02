from PyQt5 import QtCore, QtGui, QtWidgets

from add_new_product import Ui_window_anp
from add_new_vendor import Ui_window_anv
from window_bill import Ui_window_bill

 #Add this
        #self.create_new_bill.clicked.connect(self.createNewBill)
        # self.edit_bill.clicked.connect(self.editBill)
        # self.add_vendor.clicked.connect(self.addVendor)
        # self.add_product.clicked.connect(self.addProduct)  
   
# BELOW THIS
    # def createNewBill(self):
    #     f_createNewBill(self)
    
    # def editBill(self):
    #     f_editBill(self)
    # def addVendor(self):
    #     f_addVendor(self)
    # def addProduct(self):
    #     f_addProduct(self)

    #functionsQtWidgets.QMainWindow()
def f_createNewBill(self):
    self.window_anp = QtWidgets.QMainWindow()
    self.ui = Ui_window_bill()
    self.ui.setupUi(self.window_anp)
    self.window_anp.show()

def f_editBill(self):
    self.window_anp = QtWidgets.QMainWindow()
    self.ui = Ui_window_bill()
    self.ui.setupUi(self.window_anp)
    self.window_anp.show()

def f_addVendor(self):
    self.window_anp = QtWidgets.QMainWindow()
    self.ui = Ui_window_anv()
    self.ui.setupUi(self.window_anp)
    self.window_anp.show()
def f_addProduct(self):
    self.window_anp = QtWidgets.QDialog()
    self.ui = Ui_window_anp()
    self.ui.setupUi(self.window_anp)
    self.window_anp.show()