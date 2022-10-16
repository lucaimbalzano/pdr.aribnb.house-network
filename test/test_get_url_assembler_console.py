# Dreams without Goals are just Dreams
#
# - @lucaimbalzano




from cgi import test
from pip import main
import urllib3
import main 
import settings
import requests
from airbnb_url.url_assembler import url_to_search_master_assembler

@test
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
    # print('example of address: Corso Sano Gottardo, Via Ugo Betti, CityLife, Via Ludovico')
    # address = input('Enter the address: ')
    # print('>> '+address)
    # print(' ')
    # print('enter a numeric number')
    # street_number = input('Enter the street number: ')
    # print('>> '+street_number)
    # print(' ')
    # print('example of city Milano, Torino, Bergamo')
    # city = input('Enter the city: ')
    # print('>> '+city)
    # print(' ')
    # print('example of province MI, BR, NO, TO..')
    # province = input('Enter the province: ')
    # print('>> '+province)
    # print(' ')
    # print('example of state Italia, Germania, ')
    # state = input('Enter the state: ')
    # print('>> '+state)
    # print(' ')
    # print('format date to enter: YEAR-MONTH-DAY')
    # date_checkin = input('Enter the checkin date: ')
    # print('>> '+ date_checkin)
    # print(' ')
    # date_checkout = input('Enter the checkout date: ')
    # print('>> '+ date_checkout)
    # print(' ')
    # adults = input('Enter quantity adults: ')
    # print('>> '+ adults)
    # print(' ')

    address ='Via Ugo Betti'
    street_number = '22'
    city = 'Milano'
    province = 'MI'
    state = 'Italia'
    date_checkin = '20222-11-22'
    date_checkout = '2022-11-27'
    adults = '4'

    # address_lng_lat = 'Via Ugo Betti 22, Milano, MI Italia'
    address_lng_lat = address + ' ' + street_number + ', ' + city + ', ' + province + ' ' + state
    url = 'https://nominatim.openstreetmap.org/search/' + urllib3.parse.quote(address_lng_lat) +'?format=json'
    response = requests.get(url).json()
    lat = response[0]["lat"]
    lng = response[0]["lon"]

    return url_to_search_master_assembler(settings.BASE_URL,address,street_number,city,province,state, date_checkin,date_checkout, lat, lng, adults)