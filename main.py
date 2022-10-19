# coding=utf-8
# Dreams without Goals are just Dreams
#
# - @lucaimbalzano
import time
import traceback

import settings.settings
from airbnb_url.url_assembler import url_to_search_master_assembler_selenium
from airbnb_url.url_assembler_selenium import get_page2, get_page3, get_search_address
from airbnb_scraping.airbnb_extraction import core_extraction

from console.get_url_assembler_console import get_input_console
from console.log.logger import get_logger

from cronometer import ChronoMeter
from utils import write_excel
from selenium import webdriver

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
        # print('X')
        # time.sleep(4)

        for i_letter_cell in range(0,len(CELL_COLUMN_TO_FILL)-1):
            for i_url_based_checkinout in range(0, len(input_console_data.check_inout_list)-1):
                url_retrived = url_to_search_master_assembler_selenium(input_console_data.address,
                                                                       input_console_data.check_inout_list[i_url_based_checkinout].date_checkin,
                                                                       input_console_data.check_inout_list[i_url_based_checkinout].date_checkout,
                                                                       input_console_data.lat, input_console_data.lng,
                                                                       input_console_data.adults)
                #TODO i'll change with a dinamic number
                for i in range(0,3):
                    if (i == 0):
                       houses_airbnb.append(core_extraction(url_retrived))
                    if (i == 1):
                        url = get_page2(url_retrived)
                        houses_airbnb.append(core_extraction(url))
                    if(i == 2):
                        url = get_page3(url_retrived)
                        houses_airbnb.append(core_extraction(url))

                write_excel.write_excel_by_data_retrived(houses_airbnb, CELL_COLUMN_TO_FILL[i_letter_cell],None)
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
