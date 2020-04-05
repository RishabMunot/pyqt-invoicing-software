
# add this below call of retranslate

        # from functions_bill import setForm
        # setForm(self)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QCompleter
from PyQt5.QtGui import QIcon,QValidator
from PyQt5.QtCore import pyqtSlot,QDate,QEvent,QObject
from openpyxl import Workbook
from openpyxl import load_workbook
#data
products = {}
product_names = []
vendors = {}
vendors_names = []

#inputs
el_productnames = []
products_inputs = []
vendor_inputs = []
final_outputs = []

x = ""

products_ips = [3,4,6,8]

def setForm(self):
    global x
    x = self
    self.date_edit.setDate(QDate.currentDate())
    import_data()
    group_inputs(self)
    set_functionalities(self)

def import_data():
    global products,product_names,vendors,vendors_names
    wb = load_workbook('data/products.xlsx')
    product_sheet = wb['Sheet1']
    for i in range(2,product_sheet.max_row+1):
        name = product_sheet['B'+str(i)].value
        id = product_sheet['A'+str(i)].value
        uom = product_sheet['C'+str(i)].value
        hsn = product_sheet['D'+str(i)].value
        cgst = product_sheet['E'+str(i)].value
        sgst = product_sheet['F'+str(i)].value
        products[name] = [id,name,hsn,uom,cgst,sgst]
        product_names.append(name)
    
    wb = load_workbook('data/vendors.xlsx')
    product_sheet = wb['Sheet1']
    for i in range(2,product_sheet.max_row+1):
        name = product_sheet['A'+str(i)].value
        line1 = product_sheet['B'+str(i)].value
        line2 = product_sheet['C'+str(i)].value
        city = product_sheet['D'+str(i)].value
        dist = product_sheet['E'+str(i)].value
        state = product_sheet['F'+str(i)].value
        pincode = product_sheet['G'+str(i)].value
        gstNO = product_sheet['H'+str(i)].value
        panNo = product_sheet['I'+str(i)].value
        vendors[name] = [name,line1,line2,city,dist,state,pincode,gstNO,panNo]
        vendors_names.append(name)
    
def group_inputs(self):
    global el_productnames,products_inputs,vendor_inputs,final_outputs
    el_productnames.append(self.p_desc_1)
    el_productnames.append(self.p_desc_2)
    el_productnames.append(self.p_desc_3)
    el_productnames.append(self.p_desc_4)
    el_productnames.append(self.p_desc_5)
    el_productnames.append(self.p_desc_6)
    el_productnames.append(self.p_desc_7)
    el_productnames.append(self.p_desc_8)
    el_productnames.append(self.p_desc_9)
    el_productnames.append(self.p_desc_10)
    el_productnames.append(self.p_desc_11)
    el_productnames.append(self.p_desc_12)
    el_productnames.append(self.p_desc_13)
    el_productnames.append(self.p_desc_14)
    el_productnames.append(self.p_desc_15)

    products_inputs.append([self.p_desc_1,self.p_hsn_1,self.p_uom_1,self.p_qty_1,self.p_rate_1,self.p_taxval_1,
    self.p_gst_per_1,self.p_gst_amt_1,self.p_sgst_per_1,self.p_sgst_amt_1,self.p_total_1])
    
    products_inputs.append([self.p_desc_2,self.p_hsn_2,self.p_uom_2,self.p_qty_2,self.p_rate_2,self.p_taxval_2,
    self.p_gst_per_2,self.p_gst_amt_2,self.p_sgst_per_2,self.p_sgst_amt_2,self.p_total_2])

    products_inputs.append([self.p_desc_3,self.p_hsn_3,self.p_uom_3,self.p_qty_3,self.p_rate_3,self.p_taxval_3,
    self.p_gst_per_3,self.p_gst_amt_3,self.p_sgst_per_3,self.p_sgst_amt_3,self.p_total_3])
    
    products_inputs.append([self.p_desc_4,self.p_hsn_4,self.p_uom_4,self.p_qty_4,self.p_rate_4,self.p_taxval_4,
    self.p_gst_per_4,self.p_gst_amt_4,self.p_sgst_per_4,self.p_sgst_amt_4,self.p_total_4])

    products_inputs.append([self.p_desc_5,self.p_hsn_5,self.p_uom_5,self.p_qty_5,self.p_rate_5,self.p_taxval_5,
    self.p_gst_per_5,self.p_gst_amt_5,self.p_sgst_per_5,self.p_sgst_amt_5,self.p_total_5])
    
    products_inputs.append([self.p_desc_6,self.p_hsn_6,self.p_uom_6,self.p_qty_6,self.p_rate_6,self.p_taxval_6,
    self.p_gst_per_6,self.p_gst_amt_6,self.p_sgst_per_6,self.p_sgst_amt_6,self.p_total_6])

    products_inputs.append([self.p_desc_7,self.p_hsn_7,self.p_uom_7,self.p_qty_7,self.p_rate_7,self.p_taxval_7,
    self.p_gst_per_7,self.p_gst_amt_7,self.p_sgst_per_7,self.p_sgst_amt_7,self.p_total_7])
    
    products_inputs.append([self.p_desc_8,self.p_hsn_8,self.p_uom_8,self.p_qty_8,self.p_rate_8,self.p_taxval_8,
    self.p_gst_per_8,self.p_gst_amt_8,self.p_sgst_per_8,self.p_sgst_amt_8,self.p_total_8])

    products_inputs.append([self.p_desc_9,self.p_hsn_9,self.p_uom_9,self.p_qty_9,self.p_rate_9,self.p_taxval_9,
    self.p_gst_per_9,self.p_gst_amt_9,self.p_sgst_per_9,self.p_sgst_amt_9,self.p_total_9])
    
    products_inputs.append([self.p_desc_10,self.p_hsn_10,self.p_uom_10,self.p_qty_10,self.p_rate_10,self.p_taxval_10,
    self.p_gst_per_10,self.p_gst_amt_10,self.p_sgst_per_10,self.p_sgst_amt_10,self.p_total_10])

    products_inputs.append([self.p_desc_11,self.p_hsn_11,self.p_uom_11,self.p_qty_11,self.p_rate_11,self.p_taxval_11,
    self.p_gst_per_11,self.p_gst_amt_11,self.p_sgst_per_11,self.p_sgst_amt_11,self.p_total_11])
    
    products_inputs.append([self.p_desc_12,self.p_hsn_12,self.p_uom_12,self.p_qty_12,self.p_rate_12,self.p_taxval_12,
    self.p_gst_per_12,self.p_gst_amt_12,self.p_sgst_per_12,self.p_sgst_amt_12,self.p_total_12])
    
    products_inputs.append([self.p_desc_13,self.p_hsn_13,self.p_uom_13,self.p_qty_13,self.p_rate_13,self.p_taxval_13,
    self.p_gst_per_13,self.p_gst_amt_13,self.p_sgst_per_13,self.p_sgst_amt_13,self.p_total_13])

    products_inputs.append([self.p_desc_14,self.p_hsn_14,self.p_uom_14,self.p_qty_14,self.p_rate_14,self.p_taxval_14,
    self.p_gst_per_14,self.p_gst_amt_14,self.p_sgst_per_14,self.p_sgst_amt_14,self.p_total_14])
    
    products_inputs.append([self.p_desc_15,self.p_hsn_15,self.p_uom_15,self.p_qty_15,self.p_rate_15,self.p_taxval_15,
    self.p_gst_per_15,self.p_gst_amt_15,self.p_sgst_per_15,self.p_sgst_amt_15,self.p_total_15])
    
    vendor_inputs = [self.vendor_name,self.add_line1,self.add_line2,self.add_city,self.add_district,self.add_state,self.add_pincode,self.vedor_gst_no,self.vendor_pan_no]

    final_outputs = [self.total_qty,self.total_tax_val,self.total_cgst_amt,self.total_sgst_amt, self.total_total,self.amt_bt,self.amt_cgst,self.amt_sgst,self.amt_gst,self.amt_at]

def set_functionalities(self):

#adding completers
    completer = QCompleter(product_names)
    completer.setCaseSensitivity(False)
    for i in range(15):
        el_productnames[i].setCompleter(completer)


#Listner on product name
    el_productnames[0].editingFinished.connect(lambda:fillDataProduct(1))
    el_productnames[1].editingFinished.connect(lambda:fillDataProduct(2))
    el_productnames[2].editingFinished.connect(lambda:fillDataProduct(3))
    el_productnames[3].editingFinished.connect(lambda:fillDataProduct(4))
    el_productnames[4].editingFinished.connect(lambda:fillDataProduct(5))
    el_productnames[5].editingFinished.connect(lambda:fillDataProduct(6))
    el_productnames[6].editingFinished.connect(lambda:fillDataProduct(7))
    el_productnames[7].editingFinished.connect(lambda:fillDataProduct(8))
    el_productnames[8].editingFinished.connect(lambda:fillDataProduct(9))
    el_productnames[9].editingFinished.connect(lambda:fillDataProduct(10))
    el_productnames[10].editingFinished.connect(lambda:fillDataProduct(11))
    el_productnames[11].editingFinished.connect(lambda:fillDataProduct(12))
    el_productnames[12].editingFinished.connect(lambda:fillDataProduct(13))
    el_productnames[13].editingFinished.connect(lambda:fillDataProduct(14))
    el_productnames[14].editingFinished.connect(lambda:fillDataProduct(15))

#Listner on rate
    products_inputs[0][4].editingFinished.connect(lambda:fillValues(1))
    products_inputs[1][4].editingFinished.connect(lambda:fillValues(2))
    products_inputs[2][4].editingFinished.connect(lambda:fillValues(3))
    products_inputs[3][4].editingFinished.connect(lambda:fillValues(4))
    products_inputs[4][4].editingFinished.connect(lambda:fillValues(5))
    products_inputs[5][4].editingFinished.connect(lambda:fillValues(6))
    products_inputs[6][4].editingFinished.connect(lambda:fillValues(7))
    products_inputs[7][4].editingFinished.connect(lambda:fillValues(8))
    products_inputs[8][4].editingFinished.connect(lambda:fillValues(9))
    products_inputs[9][4].editingFinished.connect(lambda:fillValues(10))
    products_inputs[10][4].editingFinished.connect(lambda:fillValues(11))
    products_inputs[11][4].editingFinished.connect(lambda:fillValues(12))
    products_inputs[12][4].editingFinished.connect(lambda:fillValues(13))
    products_inputs[13][4].editingFinished.connect(lambda:fillValues(14))
    products_inputs[14][4].editingFinished.connect(lambda:fillValues(15))

#Listner on qty
    products_inputs[0][3].editingFinished.connect(lambda:fillValues(1))
    products_inputs[1][3].editingFinished.connect(lambda:fillValues(2))
    products_inputs[2][3].editingFinished.connect(lambda:fillValues(3))
    products_inputs[3][3].editingFinished.connect(lambda:fillValues(4))
    products_inputs[4][3].editingFinished.connect(lambda:fillValues(5))
    products_inputs[5][3].editingFinished.connect(lambda:fillValues(6))
    products_inputs[6][3].editingFinished.connect(lambda:fillValues(7))
    products_inputs[7][3].editingFinished.connect(lambda:fillValues(8))
    products_inputs[8][3].editingFinished.connect(lambda:fillValues(9))
    products_inputs[9][3].editingFinished.connect(lambda:fillValues(10))
    products_inputs[10][3].editingFinished.connect(lambda:fillValues(11))
    products_inputs[11][3].editingFinished.connect(lambda:fillValues(12))
    products_inputs[12][3].editingFinished.connect(lambda:fillValues(13))
    products_inputs[13][3].editingFinished.connect(lambda:fillValues(14))
    products_inputs[14][3].editingFinished.connect(lambda:fillValues(15))

#Listner on CSGT
    products_inputs[0][6].editingFinished.connect(lambda:fillValues(1))
    products_inputs[1][6].editingFinished.connect(lambda:fillValues(2))
    products_inputs[2][6].editingFinished.connect(lambda:fillValues(3))
    products_inputs[3][6].editingFinished.connect(lambda:fillValues(4))
    products_inputs[4][6].editingFinished.connect(lambda:fillValues(5))
    products_inputs[5][6].editingFinished.connect(lambda:fillValues(6))
    products_inputs[6][6].editingFinished.connect(lambda:fillValues(7))
    products_inputs[7][6].editingFinished.connect(lambda:fillValues(8))
    products_inputs[8][6].editingFinished.connect(lambda:fillValues(9))
    products_inputs[9][6].editingFinished.connect(lambda:fillValues(10))
    products_inputs[10][6].editingFinished.connect(lambda:fillValues(11))
    products_inputs[11][6].editingFinished.connect(lambda:fillValues(12))
    products_inputs[12][6].editingFinished.connect(lambda:fillValues(13))
    products_inputs[13][6].editingFinished.connect(lambda:fillValues(14))
    products_inputs[14][6].editingFinished.connect(lambda:fillValues(15))

#Listner on SGST
    products_inputs[0][8].editingFinished.connect(lambda:fillValues(1))
    products_inputs[1][8].editingFinished.connect(lambda:fillValues(2))
    products_inputs[2][8].editingFinished.connect(lambda:fillValues(3))
    products_inputs[3][8].editingFinished.connect(lambda:fillValues(4))
    products_inputs[4][8].editingFinished.connect(lambda:fillValues(5))
    products_inputs[5][8].editingFinished.connect(lambda:fillValues(6))
    products_inputs[6][8].editingFinished.connect(lambda:fillValues(7))
    products_inputs[7][8].editingFinished.connect(lambda:fillValues(8))
    products_inputs[8][8].editingFinished.connect(lambda:fillValues(9))
    products_inputs[9][8].editingFinished.connect(lambda:fillValues(10))
    products_inputs[10][8].editingFinished.connect(lambda:fillValues(11))
    products_inputs[11][8].editingFinished.connect(lambda:fillValues(12))
    products_inputs[12][8].editingFinished.connect(lambda:fillValues(13))
    products_inputs[13][8].editingFinished.connect(lambda:fillValues(14))
    products_inputs[14][8].editingFinished.connect(lambda:fillValues(15))

    vendor_inputs[0].editingFinished.connect(fillVendor)

    completer = QCompleter(vendors_names)
    completer.setCaseSensitivity(False)
    self.vendor_name.setCompleter(completer)



def generateWarningForInt(x):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Input can only be a number")
    msg.setWindowTitle("Please enter number")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()
    
        
def fillDataProduct(x):
    pro = products.get(el_productnames[x-1].text())
    ip = products_inputs[x-1]
    if pro:
        ip[0].setText(pro[1])
        ip[1].setText(pro[2])
        ip[2].setText(pro[3])
        ip[6].setText(pro[4])
        ip[8].setText(pro[5])
    
def fillVendor():
    ven = vendors.get(vendor_inputs[0].text())
    if ven:
        for i in range(9):
            vendor_inputs[i].setText(ven[i])

def fillValues(x):
        
    total = 0

    try:
        qty = products_inputs[x-1][3].text()
        rate = products_inputs[x-1][4].text()
        if(qty== ""):
            products_inputs[x-1][3].setText("0")
        elif(rate == ""):
            products_inputs[x-1][4].setText("0")

        else:
            qty = int(qty)
            rate = int(rate)

        taxval = str(qty*rate)
        products_inputs[x-1][5].setText(taxval)
    except Exception:
        generateWarningForInt(x)
        pass

    try:
        taxval = products_inputs[x-1][5].text()
        cgst = products_inputs[x-1][6].text()
        sgst = products_inputs[x-1][8].text()
        if(taxval== ""):
            products_inputs[x-1][5].setText("0")            
        elif(cgst == ""):
            products_inputs[x-1][6].setText("0") 
        elif sgst == "":
            products_inputs[x-1][8].setText("0") 
        else:
            taxval = int(taxval)
            cgst = int(cgst)
            sgst = int(sgst)

        products_inputs[x-1][7].setText(str(cgst*taxval*0.01))
        products_inputs[x-1][9].setText(str(sgst*taxval*0.01))

        total = taxval + cgst + sgst
        products_inputs[x-1][10].setText(str(sgst*taxval*0.01))


    except Exception:
        generateWarningForInt(x)
        pass

    fillFinalValues()

def fillFinalValues():
    tot_qty = 0
    tot_taxval = 0
    tot_sgst = 0
    tot_cgst = 0
    tot_total = 0
    for i in range(15):
        tot_qty += int(products_inputs[i][3].text())
        tot_taxval += float(products_inputs[i][5].text())
        tot_sgst += float(products_inputs[i][9].text())
        tot_cgst += float(products_inputs[i][7].text())
        tot_total += float(products_inputs[i][10].text())
    
    final_outputs[0].setText(str(tot_qty))
    final_outputs[1].setText(str(tot_taxval))
    final_outputs[2].setText(str(tot_cgst))
    final_outputs[3].setText(str(tot_sgst))
    final_outputs[4].setText(str(tot_total))
    final_outputs[5].setText(str(tot_taxval))
    final_outputs[6].setText(str(tot_cgst))
    final_outputs[7].setText(str(tot_sgst))
    final_outputs[8].setText(str(tot_cgst+tot_sgst))
    final_outputs[9].setText(str(tot_total))