# Add this below class
    # def clear_data(self):
    #     print('clear')
    # def add_vendor(self):
    #     print('add')

from openpyxl import Workbook
from openpyxl import load_workbook

def f_clear_data(self):
    self.vendor_name.setText("")
    self.add_line1.setText("")
    self.add_line2.setText("")
    self.add_city.setText("")
    self.add_pincode.setText("")
    self.add_district.setText("")
    self.add_state.setText("")
    self.vedor_gst_no.setText("")
    self.vendor_pan_no.setText("")
    self.vendor_name.setText("")

def f_add_vendor(self):
    name = self.vendor_name.text()
    line1 = self.add_line1.text()
    line2 = self.add_line2.text()
    city = self.add_city.text()
    pincode = self.add_pincode.text()
    dist = self.add_district.text()
    state = self.add_state.text()
    gstNO= self.vedor_gst_no.text()
    panNo = self.vendor_pan_no.text()
    
    