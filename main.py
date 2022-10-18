# coding=utf-8
# Dreams without Goals are just Dreams
#
# - @lucaimbalzano
import calendar
import traceback
from logging import DEBUG, Logger
import logging
from math import lgamma
from pickletools import optimize
import sys
import requests
import urllib.parse
from airbnb_url.url_assembler import url_to_search_master_assembler_selenium
from airbnb_url.url_assembler_selenium import get_next_page, get_page2, get_page3, get_search_address
from console.get_url_assembler_console import get_input_console
from console.log.logger import get_logger
from dto.calendar_filled import get_calendar_filled
from dto.checkin_checkout import Checkin_checkout
from dto.year_month_day import Year_Month_Day
from settings import settings
from airbnb_scraping.airbnb_extraction import core_extraction
from cronometer import ChronoMeter

import time

from datetime import datetime
from datetime import timedelta
from datetime import date
from airbnb_url import url_defraction_lat_lng
from utils import write_excel
import console.log

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()
houses_airbnb = []


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

    try:

        # 1MONTH  1MONTHWEEK 3MONTH  3MONTHWEEK 6MONTH  6MONTHWEEK
        # C14:38  D14:38     E14:38   F14:38    G14:38  H14:38    [X14:76]

        CELL_COLUMN_TO_FILL = ['C','D','E','F','G','H']

        # url_retrived = get_link_search_houses_by_input_user_selenium(browser)
                            # insideofupper: return


        input_console_data = get_input_console(browser)

        for index_cells_to_fill in range(0,len(CELL_COLUMN_TO_FILL)):

            for i in range(3):
                if (i == 0):
                    url_retrived = url_to_search_master_assembler_selenium(input_console_data.address, input_console_data.checkin_checkout[0].date_checking,
                                                                           input_console_data.checkin_checkout[
                                                                               0].date_checkout, input_console_data.lat, input_console_data.lng, input_console_data.adults)
                    houses_airbnb.append(core_extraction(url_retrived))
                    houses_airbnb.append(core_extraction(url_retrived))

                if (i == 1):
                    url_retrived = url_to_search_master_assembler_selenium(input_console_data.address,
                                                                           input_console_data.checkin_checkout[
                                                                               1].date_checking,
                                                                           input_console_data.checkin_checkout[
                                                                               1].date_checkout, input_console_data.lat,
                                                                           input_console_data.lng,
                                                                           input_console_data.adults)
                    url = get_page2(url_retrived)
                    houses_airbnb.append(core_extraction(url))

                if (i == 2):
                    url_retrived = url_to_search_master_assembler_selenium(input_console_data.address,
                                                                           input_console_data.checkin_checkout[
                                                                               2].date_checking,
                                                                           input_console_data.checkin_checkout[
                                                                               2].date_checkout, input_console_data.lat,
                                                                           input_console_data.lng,
                                                                           input_console_data.adults)
                    url = get_page3(url_retrived)
                    houses_airbnb.append(core_extraction(url))

                write_excel.write_excel_by_data_retrived(houses_airbnb, CELL_COLUMN_TO_FILL[index_cells_to_fill])
                houses_airbnb = []

    except Exception as e:
        print('[ERROR] - '+str(e))
        traceback.print_exc()
    except PermissionError as pe:
        logger.error('Error occurred: Check if the file is already open in the current computer; Message: '+str(pe))
        traceback.print_exc()
    finally:
        chrono.stop_chrono()
        chrono.print_time()
        browser.close()
        exit(1)
