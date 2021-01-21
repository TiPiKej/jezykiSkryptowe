import json
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
try:
    with open("zadanie11.json", "r") as json_file:
        dane = json.load(json_file)
        for komorka in dane:
            ws.cell(row=komorka['row'], column=komorka['column']).value = komorka['value']
            print(komorka)
        wb.save("zadanie11.xlsx")
except IOError:
    print("Blad IO")
