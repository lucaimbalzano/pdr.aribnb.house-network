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




def get_next_page(browser):
    scroll_to_footer_paginations(browser)
    try:
        btn_next_page = browser.find_element(By.CLASS_NAME, "_1bfat5l").click()
        logger.info('>> Next page clicked with success')
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


def get_search_address(browser):
    time.sleep(2)
    open_searchbox = browser.find_element(By.CLASS_NAME, 'f19g2zq0').click()
    time.sleep(2)

    form_textfield_address = browser.find_element(By.NAME, 'query')
    form_textfield_address.send_keys("Via Ugo Betti 22, Milano MI Italia")    
    btn_search = browser.find_element(By.CLASS_NAME, "b134py57").click()

    return get_next_page(browser)

def get_page2(url):
    print('[DEBUG] - PAGE2:: '+url+page2)
    return url + page2;

def get_page3(url):
    print('[DEBUG] - PAGE3:: '+url+page3)
    return url + page3;