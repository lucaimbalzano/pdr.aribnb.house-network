# Dreams without Goals are just Dreams
#
# - @lucaimbalzano



from importlib.resources import path
from openpyxl import Workbook, worksheet, load_workbook
from os import listdir
import os
import openpyxl
from settings.settings import PREFIX_URL_EXCEL
from console.log.logger import get_logger

logger = get_logger()

def write_excel_by_column(start_cell_column,start_cell_row,  data_to_write, ws):
    # C14:38 
    start_cell = 'C'
    start_cell_row = 14
    for page in range(len(data_to_write)):
        for i in range(start_cell_row, page):
            if(i % 2 == 0):
                # print("[DEBUG] - price: "+[data_to_write[page][i].price])
                ws.append([data_to_write[page][i].price])    
            else:
                print("[DEBUG] - url: "+[data_to_write[page][i].url])
                # ws.append(PREFIX_URL_EXCEL + [data_to_write[page][i].url])
                
                 
def write_excel_by_column(start_cell_column,start_cell_row, last_column_index_value, data_to_write, ws):
    # C14:38 
    start_cell = 'C'
    # start_cell_row = 14
    # for page in range(len(data_to_write)):
    #     for i in range(start_cell_row, last_column_index_value):
    #         for data_house_index_in_array in range(len(data_to_write[page])):
    #             if(i % 2 == 0):
    #                 print("[DEBUG] - price: "+str([data_to_write[i].price]))
    #                 ws['C'+str(i)] = data_to_write[page].price
    #             else:
    #                 print("[DEBUG] - url: "+str([data_to_write[page].url]))
    #                 ws['C'+str(i)] = PREFIX_URL_EXCEL + data_to_write[page].url
    pages_length = 2

    row = '14'
    row_index = 14

    print('[DEBUG] - rowIndex : 14, '+ str(len(data_to_write)*len(data_to_write[0])))
    for row_index in range(row_index, len(data_to_write)*len(data_to_write[0])):
            try:
                for page in (0, pages_length):
                    for index_house in range(0, len(data_to_write[page])):
                        current_index_house = index_house
                        house = data_to_write[page][index_house]

                        if (row_index % 2 == 0):
                            # print("[DEBUG] - price: " + str(house.price))
                            logger.debug("price: "+str(house.price))
                            index_house = row_index + index_house
                            cell_to_write = 'C' + str(index_house)
                            ws[cell_to_write] = int(house.price)
                        else:
                            # print("[DEBUG] - url: " + str(house.url))
                            logger.debug("url: " + str(house.url))
                            index_house = row_index + index_house
                            cell_to_write = 'C' + str(row_index)
                            ws[cell_to_write] = PREFIX_URL_EXCEL + house.url

                        index_house = current_index_house

            except Exception as e:
                print("write-excel::write_excel_by_column - Error Occured: "+str(e))
                logger.error("write-excel::write_excel_by_column - Error Occured: "+str(e))
            finally:
                None



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

    assert os.path.isfile(path)
    wb.save(path)
    wb.close()