from openpyxl import load_workbook

load_wb = load_workbook("./test1.xlsx", data_only=True)
load_ws = load_wb["Sheet1"]

# print(load_ws['A1'].value)
'''
get_cells = load_ws['A1':'D2']
for row in get_cells:
    for cell in row:
        print(cell.value)
'''
for row in load_ws.rows:
    print(row.value)