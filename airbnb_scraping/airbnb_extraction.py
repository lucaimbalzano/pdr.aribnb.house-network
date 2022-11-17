# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

from time import sleep
import requests
import re
from bs4 import BeautifulSoup
from requests import get
from airbnb_url.url_defraction_lat_lng import defraction_url_lat_lng, moving_map_nwse_calculation
from console.log.logger import get_logger
from dto.data_immobile import Data_immobile
from settings import settings, settings_access_tag as settingTAG
from selenium.webdriver.common.by import By

logger = get_logger()

def click_btn_zoom_in_map(browser):
    try:
        zoom_in_map = browser.find_element( By.XPATH, settingTAG.ZOOM_IN_BTN )
        zoom_in_map.click()
        sleep(1)
    except Exception as e:
        print('[ERROR] Error while trying clicking zoom in btn: '+str(e))
        pass

def click_btn_zoom_out_map(browser):
    try:
        zoom_out_map = browser.find_element( By.XPATH, settingTAG.ZOOM_OUT_BTN )
        zoom_out_map.click()
        sleep(1)
    except Exception as e:
       print('[ERROR] Error while trying clicking zoom out btn: '+str(e))
       pass

def getPageZoomedBasedOnHousesFounded(url_with_lat_lng, url_next_page, checkin_date, checkout_date, browser):
    try:
        counter_support = 0
        
        while(True):
            if counter_support == 0:
                url_to_check = url_next_page
            else:
                browser.get(url_to_check)
           
            houses_found = browser.find_element(By.CLASS_NAME, settingTAG.HEAD_COUNTER_HOUSES).text.split('\n')[1].split(' ')
            if 'Over' in houses_found[0]:
                click_btn_zoom_in_map(browser)
                counter_support += 1
                url_to_check = browser.current_url
            
            elif int(houses_found[0]) < 15 and counter_support < 7:
                click_btn_zoom_out_map(browser)
                counter_support += 1
                url_to_check = browser.current_url
            
            elif int(houses_found[0]) < 15 and counter_support == 2:
                url_NORD_NWSE = moving_map_nwse_calculation(url_with_lat_lng, defraction_url_lat_lng(url_with_lat_lng, 'search_type=search_query&'), settings.MOVING_TO_VALUES_NWSE[0],  checkin_date, checkout_date)
                url_to_check = url_NORD_NWSE
                browser.get(url_to_check)
                click_btn_zoom_in_map(browser)
                counter_support += 1
            
            elif int(houses_found[0]) < 15 and counter_support == 3:
                url_SUD_NWSE = moving_map_nwse_calculation(url_with_lat_lng, defraction_url_lat_lng(url_with_lat_lng, 'search_type=search_query&'), settings.MOVING_TO_VALUES_NWSE[1],  checkin_date, checkout_date)
                url_to_check = url_SUD_NWSE
                browser.get(url_to_check)
                click_btn_zoom_in_map(browser)
                counter_support += 1
            
            elif int(houses_found[0]) < 15 and counter_support == 4:
                url_WEST_NWSE = moving_map_nwse_calculation(url_with_lat_lng, defraction_url_lat_lng(url_with_lat_lng, 'search_type=search_query&'), settings.MOVING_TO_VALUES_NWSE[2],  checkin_date, checkout_date)
                url_to_check = url_WEST_NWSE
                browser.get(url_to_check)
                click_btn_zoom_in_map(browser)
                counter_support += 1
            
            elif int(houses_found[0]) < 15 and counter_support == 5:
                url_EST_NWSE = moving_map_nwse_calculation(url_with_lat_lng, defraction_url_lat_lng(url_with_lat_lng, 'search_type=search_query&'), settings.MOVING_TO_VALUES_NWSE[3],  checkin_date, checkout_date)
                url_to_check = url_EST_NWSE
                browser.get(url_to_check)
                click_btn_zoom_in_map(browser)
                counter_support += 1
            
            else:
                print('[DEBUG] homes in this page: '+str(houses_found[0]))
                return url_to_check
                break    

    except Exception as e:
        try:
            print("[ERROR] no houses retrived: "+browser.find_element(By.CLASS_NAME, settingTAG.NO_HOUSES_MATCHED).text)
        except Exception:
            print('[ERROR] error not checkable')
            pass
        pass
    


def get_price_by_dirty_format(price_str):
    price = ''
    for elems in price_str:
        if (elems == '€'):
            return price;
        if (re.match('^[-+]?[0-9]+$', elems)):
            price = price + elems


def get_all_link_page(soup, url):
    # TESTS

    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 104.0.0.0 Safari / 537.36'
    }
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # Mozilla / 5.0(Windows NT 10.0) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 104.0.0.0 Safari / 537.36
    res = get(url, headers=headers)
    soup = BeautifulSoup(res.text, features="html.parser")
    url_list = soup.find_all("meta", attrs={"itemprop": "url"})

    html_list_pagination = soup.find_all('div', 'c1yo0219')
    print(html_list_pagination.prettify())
    # all_links = soup.find_all('div','_jro6t0')
    # soup.find("div", {"class": "c1bp99s5 dir dir-ltr"})
    all_links = soup.find_all('div', 'c1bp99s5')
    a_link = all_links[0].find('a', href=True)
    print(all_links[0].find('a').contents[0])


def extraction_by_soup(soup, max_price_threshold):
    house_airbnb_list = [];
    house_airbnb = None
    html_list = soup.find_all('div', 'gh7uyir')
    if (html_list != 0 and html_list != None and len(html_list) != 0):
        try:
            all_cards = html_list[0].find_all('div', 'c4mnd7m')
            for i in range(len(all_cards)):
                logger.debug("#### CARD N [ " + str(i) + " ] ####")

                price = all_cards[i].find_all('span', 'a8jt5op')[0].text.split('per')
                price_clean = price[0].split('$')[1].split(' ')[0]

                if int(price_clean) < (max_price_threshold*1.25):
                    cover_card = all_cards[i].find('source').get('srcset')
                    title_card_general = all_cards[i].find('div', 't1jojoys').get_text()
                    title_card_detail = all_cards[i].find('div', 'nquyp1l').get_text()
                    all_meta = all_cards[i].find_all('meta')

                    if (len(all_meta) == 3):
                        urls = all_meta[2].get("content")
                        logger.debug("URL: " + urls if urls else "url: No meta url given")
                    else:
                        urls = soup.find(itemprop="url").get("content")
                        logger.debug("URL: " + urls if urls else "url: No meta url given")

                    is_superHost = all_cards[i].find_all('div', 't1mwk1n0')
                    date_availability = all_cards[i].find_all('div', 'f15liw5s')
                

                    house_airbnb = Data_immobile(title_card_detail,
                                                urls if urls else "url: No meta url given",
                                                price_clean, None, None, None, None, None, None)
                    house_airbnb_list.append(house_airbnb)
                    # all_cards[i].find_all('span', 'a8jt5op')[1].get_text()[1:4]
                    logger.debug("price:  €" + str(price_clean))
                    logger.debug("#### END CARD N [ " + str(i) + " ] ####")
           

        except Exception as e:
            print('Error occurred: ' + e)
            logger.error('airbnb_extraction.py::extraction_by_soup() - Failed error occurred: ' + str(e))
            pass
        finally:
            return house_airbnb_list;


def core_extraction(url, max_price_threshold):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    return extraction_by_soup(soup, max_price_threshold)
