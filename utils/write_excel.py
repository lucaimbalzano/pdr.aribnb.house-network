from importlib.resources import path
from openpyxl import Workbook, worksheet, load_workbook
from os import listdir
import os
import openpyxl

def write_excel_by_data_retrived():
    print(os.path)
    path = "C:\\Users\\lucai\\Documents\\Workspaces\\house-network\\pdr.aribnb.house-network\\media\\2STANDARD_PianoDiRendimento.xlsx"
    
    wb = openpyxl.load_workbook(path)
    print(wb.sheetnames)
    ws = wb['Raccolta dati AirB&B_SEMPLICE']
    ws['A1'] = 'The sky is gray.'
    wb.save(path)
    wb.close()