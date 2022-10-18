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
from console.get_url_assembler_console import get_link_search_houses_by_input_user_selenium
from console.log.logger import get_logger
from dto.checkin_checkout import Checkin_checkout
from settings import settings
from airbnb_scraping.airbnb_extraction import core_extraction
from cronometer import ChronoMeter

import time
import datetime
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


def get_date_by_today():
    dates_checking_checkout_master = []
    dates_checkin_checkout = Checkin_checkout('2022-11-22','2022-11-27' )
    dates_checking_checkout_master.append(dates_checkin_checkout)
    dates_checkin_checkout = Checkin_checkout('2022-11-22', '2022-11-27')
    dates_checking_checkout_master.append(dates_checkin_checkout)
    dates_checkin_checkout = Checkin_checkout('2022-11-22', '2022-11-27')
    dates_checking_checkout_master.append(dates_checkin_checkout)


    date_checkin = '2022-11-22'
    date_checkout = '2022-11-27'

def get_last_day_of_the_month():
    currentDate = datetime.date.today()
    return datetime.date(currentDate.year, currentDate.month, calendar.monthrange(currentDate.year, currentDate.month)[1])

def get_between_week_by_month(month_to_check):
    today = date.today()
    today_splitted_by_dash = str(today).split('-')
    month = int(today_splitted_by_dash[1])




def get_month_day_with_variation_end_month(current_month, current_day):



if __name__ == '__main__':
    print("STARTED Airbnb -> AIP::Annual Income Plan")

    today = date.today()
    print("TODAY IS: "+str(today))
    today_splitted_by_dash = str(today).split('-')
    print(str(today_splitted_by_dash[0]))
    print(str(today_splitted_by_dash[1]))
    print(str(today_splitted_by_dash[2]))


    # logger.debug('>> STARTED - PDR::Piano Di Rendimento')
    # logger.debug('        - AIP::Annual Income Plan')
    # chrono = ChronoMeter()
    # chrono.start_chrono()
    #
    # options = get_options_web_driver()
    # browser = webdriver.Chrome('C:/Users/lucai/Documents/Utils/SW/WebDriver/106/0.5249.61/chromedriver.exe', chrome_options=options)
    # browser.get('https://www.airbnb.com')
    #
    # try:
    #     url_retrived = get_link_search_houses_by_input_user_selenium(browser)
    #
    #     for i in range(3):
    #         if (i == 0):
    #             houses_airbnb.append(core_extraction(url_retrived))
    #             houses_airbnb.append(core_extraction(url_retrived))
    #
    #         if (i == 1):
    #             url = get_page2(url_retrived)
    #             houses_airbnb.append(core_extraction(url))
    #
    #         if (i == 2):
    #             url = get_page3(url_retrived)
    #             houses_airbnb.append(core_extraction(url))
    #             write_excel.write_excel_by_data_retrived(houses_airbnb)
    #
    # except Exception as e:
    #     print('[ERROR] - '+str(e))
    #     traceback.print_exc()
    # except PermissionError as pe:
    #     logger.error('Error occurred: Check if the file is already open in the current computer; Message: '+str(pe))
    #     traceback.print_exc()
    # finally:
    #     chrono.stop_chrono()
    #     chrono.print_time()
    #     browser.close()
    #     exit(1)

    
