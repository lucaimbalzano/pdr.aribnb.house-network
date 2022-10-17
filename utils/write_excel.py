# Dreams without Goals are just Dreams
#
# - @lucaimbalzano



from importlib.resources import path
from openpyxl import Workbook, worksheet, load_workbook
from os import listdir
import os
import openpyxl
from settings.settings import PREFIX_URL_EXCEL 

def write_excel_by_column(start_cell_column,start_cell_row, last_column_index_value, data_to_write, ws):
    # C14:38 
    start_cell = 'C'
    start_cell_row = 14
    for page in range(len(data_to_write)):
        for i in range(start_cell_row, page):
            if(i % 2 == 0):
                print("[DEBUG] - price: "+[data_to_write[page][i].price])
                ws.append([data_to_write[page][i].price])    
            else:
                print("[DEBUG] - url: "+[data_to_write[page][i].url])
                ws.append(PREFIX_URL_EXCEL + [data_to_write[page][i].url])    

    

def write_excel_by_data_retrived(houses_airbnb):
    print(os.path)
    path = "C:\\Users\\lucai\\Documents\\Workspaces\\house-network\\pdr.aribnb.house-network\\media\\2STANDARD_PianoDiRendimento.xlsx"
    
    wb = openpyxl.load_workbook(path)
    print(wb.sheetnames)
    ws = wb['Raccolta_Dati_Airbnb_0']

    # 1MONTH  1MONTHWEEK 3MONTH  3MONTHWEEK 6MONTH  6MONTHWEEK   
    # C14:38  D14:38     E14:38   F14:38    G14:38  H14:38    [X14:76]

   
    # ws['A1'] = 'The sky is gray.'
    write_excel_by_column('C', 14,76,houses_airbnb,ws)


    wb.save(path)
    wb.close()