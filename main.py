# coding=utf-8
# Dreams without Goals are just Dreams
#
# - @lucaimbalzano
import time
import traceback
from airbnb_url.url_defraction_lat_lng import defraction_url_lat_lng, moving_map_nwse_calculation

from settings import settings
from settings import settings_access_tag as settingTAG
from airbnb_url.url_assembler import url_to_search_master_assembler_selenium
from airbnb_url.url_assembler_selenium import get_page2, get_page3, get_search_address, scroll_to_footer_paginations
from airbnb_scraping.airbnb_extraction import core_extraction, getPageZoomedBasedOnHousesFounded

from console.get_url_assembler_console import get_input_console
from console.log.logger import get_logger

from cronometer import ChronoMeter
from utils import write_excel
from selenium import webdriver
from selenium.webdriver.common.by import By


from utils.write_excel import open_excel, close_excel

logger = get_logger()
houses_airbnb_pages = []
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
    browser = webdriver.Chrome(settings.CHROMEDRIVER_PATH, chrome_options=options)
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
                pages_to_scroll = 4
                
                for i in range(0, pages_to_scroll):
                    if (i == 0):
                        print('[DEBUG] url page '+str(i)+': ' + url_retrived)
                        houses_airbnb_pages.append(core_extraction(url_retrived, input_console_data.max_price_threshold))
                    else:
                        
                        url_next_page = ''
                        current_url = None
                        try:
                            url_next_page = browser.find_element( By.CLASS_NAME, settingTAG.NAV_NEXT_PAGE_LINK ).get_attribute('href')
                            browser.get(url_next_page)
                        except:
                            print('[ERROR] less houses than have a next page')
                            url_next_page = None
                            pass
                        
                        if url_next_page is None:
                            current_url = getPageZoomedBasedOnHousesFounded(url_retrived, browser.current_url, input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkin,  input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkout,browser)
                        else:
                            current_url = getPageZoomedBasedOnHousesFounded(url_retrived, url_next_page, input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkin,  input_console_data.check_inout_list[i_url_based_checkinout_and_cell_row].date_checkout,browser)
                        if current_url != None:
                            houses_airbnb_pages.append(core_extraction(current_url, input_console_data.max_price_threshold))
                      

                if( houses_airbnb_pages is not None):                                                                                        # TODO delete : None
                    write_excel.write_excel_by_data_retrived(houses_airbnb_pages, CELL_COLUMN_TO_FILL[i_url_based_checkinout_and_cell_row],None)
                houses_airbnb_pages = []

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
