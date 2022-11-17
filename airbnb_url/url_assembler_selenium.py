# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from console.log.logger import get_logger
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# browser.get_log('browser')
logger = get_logger()
page3 =           '&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MiwiaXRlbXNfb2Zmc2V0Ijo0MCwidmVyc2lvbiI6MX0%3D'
page2 = '&items_offset=40&items_offset=20&cursor=eyJzZWN0aW9uX29mZnNldCI6MiwiaXRlbXNfb2Zmc2V0IjoyMCwidmVyc2lvbiI6MX0%3D'
# TODO Test
page4 = 'page4&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MiwiaXRlbXNfb2Zmc2V0Ijo2MCwidmVyc2lvbiI6MX0%3D'
page5 = '&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MiwiaXRlbXNfb2Zmc2V0Ijo4MCwidmVyc2lvbiI6MX0%3D'




def get_next_page(browser):
    scroll_to_footer_paginations(browser)
    try:
        btn_next_page = browser.find_element(By.CLASS_NAME, "_1bfat5l").click()
    except Exception as e:
        logger.error('url_assembler_selenium.py::get_next_page() - Failed error occurred: ' + str(e))


    time.sleep(4)
    browser.refresh()
    return str(browser.current_url)

def scroll_to_footer_paginations(browser):
    html = browser.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    browser.execute_script("window.scrollTo(0,4050)")
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,12050)")
    time.sleep(3)

def checkIfExistAlertThenCloseIt(browser):
    try:
        browser.find_element(By.CLASS_NAME, '_oda838').click()
    except Exception:
        pass



def get_search_address(browser,url):

    checkIfExistAlertThenCloseIt(browser)

    time.sleep(2)
    open_searchbox = browser.find_element(By.CLASS_NAME, 'f19g2zq0').click()
    time.sleep(2)

    form_textfield_address = browser.find_element(By.NAME, 'query')
    form_textfield_address.send_keys(url)
    btn_search = browser.find_element(By.CLASS_NAME, "b134py57").click()

    time.sleep(2)
    browser.refresh()
    return str(browser.current_url)

def get_page2(url):
    return url + page2;

def get_page3(url):
    return url + page3;