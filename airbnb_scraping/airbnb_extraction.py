import bs4
import requests
import re
from bs4 import BeautifulSoup

link = 'https://www.airbnb.it/s/Corso-San-Gottardo--Milano--MI--Italia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Corso%20San%20Gottardo%2C%20Milano%2C%20MI&place_id=EiZDb3JzbyBTYW4gR290dGFyZG8sIE1pbGFubywgTUksIEl0YWxpYSIuKiwKFAoSCZdiDwkIxIZHEYwn8Av-7lFfEhQKEgnndRI_ScGGRxGNDnTGE83_PA&date_picker_type=calendar&source=structured_search_input_header&search_type=user_map_move&ne_lat=45.45298769522644&ne_lng=9.185254798466218&sw_lat=45.44257044903232&sw_lng=9.170685039097322&zoom=16&search_by_map=true'

def get_price_by_dirty_format(price_str):
    price = ''
    for elems in price_str:
        if(elems == '€'):
            return price;
        if(re.match('^[-+]?[0-9]+$',elems)):
            price = price + elems








def core_extraction():
    # soup = bs4.BeautifulSoup(link, 'html.parser')
    # print(soup.prettify())
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    # print(soup.prettify())

    soup.findAll('div', 'c61fd4t')
    soup.find_all('div', 'gh7uyir')
    html_list = soup.find_all('div', 'gh7uyir')

   # all elements card
   # print(html_list[0].get_text())

    all_cards = html_list[0].find_all('div', 'c4mnd7m')
    print("#### CARD ####")
    # print("cards tag: "+all_cards[0])


    #TODO iterate cover url card
    cover_card = all_cards[0].find('source').get('srcset')
    print("url cover card: "+str(cover_card))

    # TODO iterate title general/detailed
    title_card_general = all_cards[0].find('div', 't1jojoys').get_text()
    print("title card general: "+str(title_card_general))
    title_card_detail = all_cards[0].find('div', 'n1v28t5c').get_text()
    print("title card detail: " + str(title_card_detail))

    #TODO iterate urls
    all_meta = all_cards[0].find_all('meta')
    urls = soup.find(itemprop="url").get("content")
    print("url: "+urls if urls else "url: No meta url given")

    #TODO iterate Kind of HOST
    is_superHost = all_cards[0].find_all('div', 't1mwk1n0')
    print(is_superHost[0].get_text() if is_superHost.__len__() > 0  else "Not SuperHost")

    date_availability = all_cards[0].find_all('div', 'f15liw5s')
    print("date: " + str(date_availability[3].get_text()))

    price = all_cards[0].find_all('span','a8jt5op')
    print("price: "+str(price[0].get_text()[0:4]))
    # print(get_price_by_dirty_format(price[0].get_text()))
    print("#### END CARD ####")
