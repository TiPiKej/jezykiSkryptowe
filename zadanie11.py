import json
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

# zawartosc pliku zadanie11.json
# [
#   {"row": 1, "column": 1, "value": 5},
#   {"row": 1, "column": 2, "value": 421},
#   {"row": 1, "column": 3, "value": 521},
#   {"row": 1, "column": 4, "value": 2},
#   {"row": 1, "column": 5, "value": 5},
#   {"row": 1, "column": 6, "value": 25},
#   {"row": 1, "column": 7, "value": 542},
#   {"row": 1, "column": 8, "value": "dsa"},
#   {"row": 1, "column": 9, "value": "2d"},
#   {"row": 2, "column": 1, "value": 3215},
#   {"row": 2, "column": 2, "value": 321421},
#   {"row": 2, "column": 3, "value": 321521},
#   {"row": 2, "column": 4, "value": 3212},
#   {"row": 2, "column": 5, "value": 3215},
#   {"row": 2, "column": 6, "value": 32125},
#   {"row": 2, "column": 7, "value": 321542},
#   {"row": 2, "column": 8, "value": "321dsa"},
#   {"row": 2, "column": 9, "value": "3212d"}
# ]

try:
    with open("zadanie11.json", "r") as json_file:
        dane = json.load(json_file)
        for komorka in dane:
            ws.cell(row=komorka['row'], column=komorka['column']).value = komorka['value']
            print(komorka)
        wb.save("zadanie11.xlsx")
except IOError:
    print("Blad IO")
