# Dreams without Goals are just Dreams
#
# - @lucaimbalzano



#EXAMPLES URL AIRBNB STRUCTURE
base_url = 'https://www.airbnb.it/s'
address = '/Corso-San-Gottardo'
street_number = '--2'
City = '--Milano'
Province = '--MI'
State = '--Italia'

kind_apt = '/homes'
tab_id = '?tab_id=home_tab'

refinement_paths = '&refinement_paths%5B%5D=%2Fhomes'
flexible_trip_lengths = '&flexible_trip_lengths%5B%5D=one_week'
price_filter_input_type = '&price_filter_input_type=0'

# query_percentage = '..'

date_picker_type = '&date_picker_type=calendar'
source = '&source=structured_search_input_header'
# search_type = '&search_type=user_map_move'
search_type = '&search_type=filter_change'

zoom = '&zoom=16'
search_by_map = '&search_by_map=true'



def split_str(s):
  return list(s)

def get_query_url_with_percetange(address_with_dash):
    address_splitted = split_str(address_with_dash)
    url_percentage = ''
    for i in range(len(address_splitted)):
        if(i+1<len(address_splitted)):
            if(address_splitted[i] == '-' and address_splitted[i+1] == '-'):
                address_splitted[i] = '%2C'
                address_splitted[i+1] == '%20'
        if(address_splitted[i] == '-'):
            address_splitted[i] = '%20'

    for j in range(len(address_splitted)):
        url_percentage = url_percentage + address_splitted[j]
    
    return url_percentage

def get_adress_without_dash(address, street_number, city, province, state):
    address_splitted = address.split(' ')
    address_dashed = ''
    for i in range(len(address_splitted)):
        if(i == 0):
            address_dashed = address_dashed + address_splitted[i]
        else:
            if(i == len(address_splitted)):
                address_dashed = address_dashed + address_splitted[i]
            else:
                address_dashed = address_dashed + '-' + address_splitted[i]
        
    return address_dashed + '--' + street_number + '--' + city + '--' + province + '--' + state; 


def get_lat_lng_for_airbnb_url_format(lat, lng):
    # ne_lat=45.499848086728065&ne_lng=9.144663972728466&sw_lat=45.48001596201159&sw_lng=9.113009613246703
    ne_lat = float(lat) + 0.01
    ne_lng = float(lng) 
    sw_lat = float(lat) - 0.01
    sw_lng = float(lng) - 0.02
    return '&ne_lat=' +str(ne_lat)+ '&ne_lng=' +str(ne_lng)+ '&sw_lat=' +str(sw_lat)+ '&sw_lng=' + str(sw_lng)

def url_to_search_master_assembler(base_url,address,street_number,city,province,state, checkin, checkout, lat, lng, adults):
    url = base_url
    address_with_dash = get_adress_without_dash(address, street_number, city, province, state)
    address_with_percentage = get_query_url_with_percetange(address_with_dash)
    checkin_checkout = '&checkin=' + checkin + '&checkout=' + checkout
    
    return url + address_with_dash + kind_apt + tab_id + refinement_paths + flexible_trip_lengths + price_filter_input_type + '&query=' + address_with_percentage + date_picker_type + source + search_type + get_lat_lng_for_airbnb_url_format(lat,lng) + zoom + search_by_map + checkin_checkout + '&adults=' +adults

def url_to_search_master_assembler_selenium(url, checkin, checkout, lat, lng, adults):
    checkin_checkout = '&checkin=' + checkin + '&checkout=' + checkout
    return url + get_lat_lng_for_airbnb_url_format(lat,lng) + zoom + checkin_checkout + '&adults=' +adults 

