# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


from dto.checkin_checkout import Checkin_checkout
from dto.input_data import InputConsole
import datetime
import urllib3
import settings
import requests
from airbnb_url.url_assembler import url_to_search_master_assembler, url_to_search_master_assembler_selenium
from airbnb_url.url_assembler_selenium import get_next_page, get_search_address
from utils.utils_date import get_range_time_stays, get_range_time_by_stays_and_stays_3MONTH, \
    get_range_time_by_stays_and_stays_6MONTH, get_stays_missing_until_friday, get_check_inout_list


def get_link_search_houses_by_input_user():
    print(' ')
    print('**enter all the answers in italian language**')
    print('::QUESTIONS::')
    print('::ADDRESS')
    print('::STREET NUMBER')
    print('::CITY')
    print('::PROVINCE')
    print('::STATE')
    print('::CHECKIN')
    print('::CHECKOUT')
    print(' ')
    print('example of address: Corso Sano Gottardo, Via Ugo Betti, CityLife, Via Ludovico')
    address = input('Enter the address: ')
    print('>> '+address)
    print(' ')
    print('enter a numeric number')
    street_number = input('Enter the street number: ')
    print('>> '+street_number)
    print(' ')
    print('example of city Milano, Torino, Bergamo')
    city = input('Enter the city: ')
    print('>> '+city)
    print(' ')
    print('example of province MI, BR, NO, TO..')
    province = input('Enter the province: ')
    print('>> '+province)
    print(' ')
    print('example of state Italia, Germania, ')
    state = input('Enter the state: ')
    print('>> '+state)
    print(' ')
    print('format date to enter: YEAR-MONTH-DAY')
    date_checkin = input('Enter the checkin date: ')
    print('>> '+ date_checkin)
    print(' ')
    date_checkout = input('Enter the checkout date: ')
    print('>> '+ date_checkout)
    print(' ')
    adults = input('Enter quantity adults: ')
    print('>> '+ adults)
    print(' ')

    # address_lng_lat = 'Via Ugo Betti 22, Milano, MI Italia'
    address_lng_lat = address + ' ' + street_number + ', ' + city + ', ' + province + ' ' + state
    url = 'https://nominatim.openstreetmap.org/search/' + urllib3.parse.quote(address_lng_lat) +'?format=json'
    response = requests.get(url).json()
    lat = response[0]["lat"]
    lng = response[0]["lon"]

    return url_to_search_master_assembler(settings.BASE_URL,address,street_number,city,province,state, date_checkin,date_checkout, lat, lng, adults)
def get_link_search_houses_by_input_user():
    print(' ')
    print('**enter all the answers in italian language**')
    print('::QUESTIONS::')
    print('::ADDRESS')
    print('::STREET NUMBER')
    print('::CITY')
    print('::PROVINCE')
    print('::STATE')
    print('::CHECKIN')
    print('::CHECKOUT')
    print(' ')
    print('example of address: Corso Sano Gottardo, Via Ugo Betti, CityLife, Via Ludovico')
    address = input('Enter the address: ')
    print('>> '+address)
    print(' ')
    print('enter a numeric number')
    street_number = input('Enter the street number: ')
    print('>> '+street_number)
    print(' ')
    print('example of city Milano, Torino, Bergamo')
    city = input('Enter the city: ')
    print('>> '+city)
    print(' ')
    print('example of province MI, BR, NO, TO..')
    province = input('Enter the province: ')
    print('>> '+province)
    print(' ')
    print('example of state Italia, Germania, ')
    state = input('Enter the state: ')
    print('>> '+state)
    print(' ')
    print('format date to enter: YEAR-MONTH-DAY')
    date_checkin = input('Enter the checkin date: ')
    print('>> '+ date_checkin)
    print(' ')
    date_checkout = input('Enter the checkout date: ')
    print('>> '+ date_checkout)
    print(' ')
    adults = input('Enter quantity adults: ')
    print('>> '+ adults)
    print(' ')

    # address_lng_lat = 'Via Ugo Betti 22, Milano, MI Italia'
    address_lng_lat = address + ' ' + street_number + ', ' + city + ', ' + province + ' ' + state
    url = 'https://nominatim.openstreetmap.org/search/' + urllib3.parse.quote(address_lng_lat) +'?format=json'
    response = requests.get(url).json()
    lat = response[0]["lat"]
    lng = response[0]["lon"]

    return url_to_search_master_assembler(settings.BASE_URL,address,street_number,city,province,state, date_checkin,date_checkout, lat, lng, adults)




def get_input_console_checkin_checkout():
    date_checkin = input('Enter the checkin date: ')
    print('>> ' + date_checkin)
    print(' ')
    date_checkout = input('Enter the checkout date: ')
    print('>> ' + date_checkout)
    print(' ')
    return Checkin_checkout(date_checkin,date_checkout)

def get_input_console_checkin_checkout_optional(stays):
    check_inout_list = []
    print('format date to enter: YEAR-MONTH-DAY')
    print('enter "x" if you want to write by your own')
    print('or write any key...')
    variable = input('>')
    if(variable == "x"):
        for i in range(0,6):
           if( i % 2 == 0):
               print('WEEKEND')
           else:
               print('INFRA')
           if ( i == 0 or i == 1):
               print(' from now 1 MONTH')
           elif ( i == 2 or i == 3 ):
               print(' from now 3 MONTH')
           elif ( i == 4 or i == 5 ):
                print(' from now 6 MONTH')
           if (i != 6):
               checkin_checkout = get_input_console_checkin_checkout()
               check_inout_list.append(checkin_checkout)
    else:
        check_inout_list = get_check_inout_list(stays)
    return check_inout_list


def get_input_console_stays_optional():
    stays = 0
    print('Default stays: '+str(3))
    print('enter "x" if you want change stays')
    print('or write any key...')
    variable = input('>')
    print(' ')
    if(variable == "x"):
        return variable
    else:
        return 3





def get_input_console(browser):
    print(' ')
    print('**enter all the answers in italian language**')
    # print('::QUESTIONS::')
    # print('::ADDRESS')
    # print('::STREET NUMBER')
    # print('::CITY')
    # print('::PROVINCE')
    # print('::STATE')
    # print('::CHECKIN')
    # print('::CHECKOUT')
    # print(' ')
    # print('example of address: ')
    # print('>> Via Ugo Betti 22, Milano, MI Italia')
    # print('>> Corso Sano Gottardo 20, Milano, MI Italia')
    # address = input('Enter the address: ')
    # print('>> '+address)
    # print(' ')
    # adults = input('Enter quantity adults: ')
    # print('>> '+ adults)
    # print(' ')
    stays = get_input_console_stays_optional()
    check_inout_list = get_input_console_checkin_checkout_optional(stays)

    print('LOADING YOUR REQUEST ..%')
    print(' ')
    #TODO delete
    stays = 3
    adults = '4'
    address = 'Via Paolo Sarpi 10, Milano, MI Italia'

    url = 'https://nominatim.openstreetmap.org/search/' + address + '?format=json'
    response = requests.get(url).json()
    lat = response[0]["lat"]
    lng = response[0]["lon"]

    address = get_search_address(browser, address)
    input_data = InputConsole(address, check_inout_list, adults, lat, lng)
    return input_data

