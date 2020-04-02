
from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook(filename = 'data/vendors.xlsx')
sheet = wb['Sheet1']

noOfVendors = sheet.max_row
print(noOfVendors)