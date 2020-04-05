
# from openpyxl import Workbook
# from openpyxl import load_workbook

# wb = load_workbook(filename = 'data/vendors.xlsx')
# sheet = wb['Sheet1']

# sheet.delete_rows(idx=2, amount=1)

# noOfVendors = sheet.max_row
# print(noOfVendors)

# wb.save(filename = 'data/vendors.xlsx')

i = 0

def x():
    global i
    i = 3

def y():
    print(i)

if __name__ == "__main__":
    print(i)
    x()
    y()