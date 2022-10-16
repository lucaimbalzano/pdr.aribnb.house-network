# coding=utf-8
# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

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
from settings import settings
from airbnb_scraping.airbnb_extraction import core_extraction
from cronometer import ChronoMeter
import datetime as dt
import time
from airbnb_url import url_defraction_lat_lng
from utils import write_excel
import console.log 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()


def get_options_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito");
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options


if __name__ == '__main__':
    print("Airbnb -> AIP::Annual Income Plan")
    logger.debug('>> STARTED - PDR::Piano Di Rendimento')
    logger.debug('        - AIP::Annual Income Plan')
    chrono = ChronoMeter()
    chrono.start_chrono()

    options = get_options_web_driver()
    browser = webdriver.Chrome('C:/Users/lucai/Documents/Utils/SW/WebDriver/106/0.5249.61/chromedriver.exe', chrome_options=options)
    browser.get('https://www.airbnb.com')
    
    url_retrived = get_link_search_houses_by_input_user_selenium(browser)
    
    for i in range(3):
        if (i == 1):
            url = get_search_address()
            #   soup = BeautifulSoup(requests.get(url).content, 'html.parser')
            core_extraction(url,browser, None)
        if( i == 2):
            # url_to_search_master_assembler_selenium(url, checkin, checkout, lat, lng, adults)
            url =  get_page2(url_retrived)
            core_extraction(url_retrived,browser, None)
        if( i == 3):
            # url_to_search_master_assembler_selenium(url, checkin, checkout, lat, lng, adults)
            get_page3(url_retrived)


    
    chrono.stop_chrono()
    chrono.print_time()       
    exit(1)    

    # write_excel.write_excel_by_data_retrived()

    
