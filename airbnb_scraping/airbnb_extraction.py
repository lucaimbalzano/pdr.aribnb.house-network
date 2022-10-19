# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import requests
import re
from bs4 import BeautifulSoup
from requests import get
from console.log.logger import get_logger
from dto.data_immobile import Data_immobile

logger = get_logger()


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


def extraction_by_soup(soup):
    house_airbnb_list = [];
    house_airbnb = None
    html_list = soup.find_all('div', 'gh7uyir')
    if (html_list != 0 and html_list != None and len(html_list) != 0):
        try:
            all_cards = html_list[0].find_all('div', 'c4mnd7m')
            for i in range(len(all_cards)):
                logger.debug("#### CARD N [ " + str(i) + " ] ####")

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
                price = all_cards[i].find_all('span', 'a8jt5op')
                if (len(str(price[1].get_text()[1:4]).split(',')) > 1):
                    print('[ERROR] - price up to 1K, price: ' + str(price[1].get_text()))
                    price = str(price[1].get_text()[1:6]).split(',')[0] + str(price[1].get_text()[1:6]).split(',')[1]
                else:
                    price = str(price[1].get_text()[1:4])

                house_airbnb = Data_immobile(title_card_detail,
                                             urls if urls else "url: No meta url given",
                                             price, None, None, None, None, None, None)
                house_airbnb_list.append(house_airbnb)
                # all_cards[i].find_all('span', 'a8jt5op')[1].get_text()[1:4]
                logger.debug("price: " + price)
                logger.debug("#### END CARD N [ " + str(i) + " ] ####")

        except Exception as e:
            print('Error occurred: ' + e)
            logger.error('airbnb_extraction.py::extraction_by_soup() - Failed error occurred: ' + str(e))
        finally:
            return house_airbnb_list;


def core_extraction(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    return extraction_by_soup(soup)
