# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import requests
import re
from bs4 import BeautifulSoup
from requests import get


def get_price_by_dirty_format(price_str):
    price = ''
    for elems in price_str:
        if(elems == '€'):
            return price;
        if(re.match('^[-+]?[0-9]+$',elems)):
            price = price + elems

def get_all_link_page(soup,url):
    # _jro6t0
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 104.0.0.0 Safari / 537.36'}
            # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # Mozilla / 5.0(Windows NT 10.0) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 104.0.0.0 Safari / 537.36
    res = get(url,headers=headers)
    soup = BeautifulSoup(res.text, features="html.parser")
    url_list = soup.find_all("meta", attrs={"itemprop": "url"})

    print('---------------------------------------------------------------------------------------------')
    html_list_pagination = soup.find_all('div', 'c1yo0219')
    print(html_list_pagination.prettify())
    # all_links = soup.find_all('div','_jro6t0')
    # soup.find("div", {"class": "c1bp99s5 dir dir-ltr"})
    all_links = soup.find_all('div', 'c1bp99s5')
    a_link = all_links[0].find('a', href=True)
    print(all_links[0].find('a').contents[0])


def extraction_by_soup(soup):
    soup.findAll('div', 'c61fd4t')
    soup.find_all('div', 'gh7uyir')
    html_list = soup.find_all('div', 'gh7uyir')
    if(html_list != 0 and html_list != None):
        all_cards = html_list[0].find_all('div', 'c4mnd7m')
        for i in range(len(all_cards)):
            print("#### CARD N [ "+ str(i) +" ] ####")
            #URL-IMAGE-COVER-CARD
            cover_card = all_cards[i].find('source').get('srcset')
            print("url cover card: "+str(cover_card))
            #TITLE
            title_card_general = all_cards[i].find('div', 't1jojoys').get_text()
            print("title card general: "+str(title_card_general))
            title_card_detail = all_cards[i].find('div', 'nquyp1l').get_text()
            print("title card detail: " + str(title_card_detail))
            #URL
            all_meta = all_cards[i].find_all('meta')
            urls = soup.find(itemprop="url").get("content")
            print("url: "+urls if urls else "url: No meta url given")
            #IS-SUPERHOST
            is_superHost = all_cards[i].find_all('div', 't1mwk1n0')
            print(is_superHost[0].get_text() if is_superHost.__len__() > 0  else "Not SuperHost")
            #DATE-AVAILABILITY
            date_availability = all_cards[i].find_all('div', 'f15liw5s')
            print("date: " + str(date_availability[3].get_text()))
            #PRICE
            price = all_cards[i].find_all('span','a8jt5op')
            print("price: "+str(price[0].get_text()[0:4]))
            print("#### END CARD N [ "+ str(i) +" ] ####")
        




def core_extraction( url,browser, soup ):
     
    if(soup != None):
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        extraction_by_soup(soup)
    else:
        soup = BeautifulSoup(browser.current_url, 'html.parser')
        extraction_by_soup()

