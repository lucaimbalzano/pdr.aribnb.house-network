# coding=utf-8
# Dreams without Goals are just Dreams
#
# - @lucaimbalzano
import time
import traceback
from airbnb_url.url_defraction_lat_lng import defraction_url_lat_lng, moving_map_nwse_calculation

from settings.settings import MOVING_TO_VALUES_NWSE
from airbnb_url.url_assembler import url_to_search_master_assembler_selenium
from airbnb_url.url_assembler_selenium import get_page2, get_page3, get_search_address, scroll_to_footer_paginations
from airbnb_scraping.airbnb_extraction import core_extraction

from console.get_url_assembler_console import get_input_console
from console.log.logger import get_logger

from cronometer import ChronoMeter
from utils import write_excel
from selenium import webdriver
from selenium.webdriver.common.by import By


from utils.write_excel import open_excel, close_excel

logger = get_logger()
houses_airbnb = []
CELL_COLUMN_TO_FILL = ['C','D','E','F','G','H']


def get_options_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito");
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options

if __name__ == '__main__':
    print("STARTED Airbnb -> AIP::Annual Income Plan")
    logger.debug('>> STARTED - PDR::Piano Di Rendimento')
    logger.debug('        - AIP::Annual Income Plan')
    chrono = ChronoMeter()
    chrono.start_chrono()

    options = get_options_web_driver()
    browser = webdriver.Chrome('C:/Users/lucai/Documents/Utils/SW/WebDriver/106/0.5249.61/chromedriver.exe', chrome_options=options)
    browser.get('https://www.airbnb.com')
    workbook_excel_open = None

    try:
        input_console_data = get_input_console(browser)
        # workbook_excel_open = open_excel(settings.settings.PATH_EXCEL)


        for i_url_based_checkinout_and_cell_row in range(0, len(input_console_data.check_inout_list)):
                print('[DEBUG] - LETTER: ' + CELL_COLUMN_TO_FILL[i_url_based_checkinout_and_cell_row] + ' ::=====================================================')
                url_retrived = url_to_search_master_assembler_selenium(input_console_data.address,
                                                                       input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkin,
                                                                       input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkout,
                                                                       input_console_data.lat, input_console_data.lng,
                                                                       input_console_data.adults)
                #TODO i'll change with a dinamic number

                for i in range(0,3):
                    if (i == 0):
                        print('[DEBUG] url page 1: ' + url_retrived)
                        houses_airbnb.append(core_extraction(url_retrived))

                        # TODO move lat and lng based on [1]- [2] [3]
                        # url_nord = moving_map_nwse_calculation(url_retrived, defraction_url_lat_lng(url_retrived, 'search_type=search_query&'), MOVING_TO_VALUES_NWSE[1],  input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkin,  input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkout)
                        
                        # href next page
                        # elems = browser.find_element(By.CLASS_NAME, '_1bfat5l')
                        # link1 = elems.get_attribute('href')
                        # zoom in map
                        # browser.find_element(By.XPATH, "//*[@id='site-content']/div[3]/div/div/div/div/div/div[2]/button[2]").click()

                    if (i == 1):
                        url = get_page2(url_retrived)
                        houses_airbnb.append(core_extraction(url))
                        print('[DEBUG] url page 2: ' + url +  ', CHECKIN: ' + input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkin + ', CHECKOUT: '+input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkout)
                    if(i == 2):
                        url = get_page3(url_retrived)
                        print('[DEBUG] url page 3: ' + url +  ', CHECKIN: ' + input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkin + ', CHECKOUT: '+input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkout)
                        houses_airbnb.append(core_extraction(url))
                if( houses_airbnb is not None):                                                                                        # TODO delete : None
                    write_excel.write_excel_by_data_retrived(houses_airbnb, CELL_COLUMN_TO_FILL[i_url_based_checkinout_and_cell_row],None)
                houses_airbnb = []

    except Exception as e:
        print('[ERROR] - '+str(e))
        traceback.print_exc()
    except PermissionError as pe:
        logger.error('Error occurred: Check if the file is already open in the current computer; Message: '+str(pe))
        traceback.print_exc()
    finally:
        # close_excel(settings.settings.PATH_EXCEL,workbook_excel_open)
        chrono.stop_chrono()
        chrono.print_time()
        browser.close()
        exit(1)
