

base_url = 'https://www.airbnb.it/s'
address = '/Corso-San-Gottardo'
street_number = '--2'
City = '--Milano'
Province = '--MI'
State = '--Italia'

refinement_paths = '&refinement_paths%5B%5D=%2Fhomes'
flexible_trip_lengths = '&flexible_trip_lengths%5B%5D=one_week'
price_filter_input_type = '&price_filter_input_type=0'

def split_str(s):
  return list(s)

def get_query_url_with_percetange():
    addr = "Corso-San-Gottardo--Milano--MI"
    address_splitted = split_str(addr)
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



