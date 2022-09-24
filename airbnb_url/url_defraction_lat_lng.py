
list_NWSE = []

def moving_to_nord_calculation(list_whole,list_lat_lng):
    ne_lat = float(list_lat_lng[0].split('=')[1])+0.00973053189324
    ne_lng = float(list_lat_lng[1].split('=')[1])+0.0031328199521
    sw_lat = float(list_lat_lng[2].split('=')[1])+0.00971727625327
    sw_lng = float(list_lat_lng[3].split('=')[1])+0.003132819952099
    url_defined = list_whole[0] + 'ne_lat=' + str(ne_lat) + '&ne_lng=' + str(ne_lng) + '&sw_lat=' + str(sw_lat) + '&sw_lng=' + str(sw_lng)
    return url_defined;

def defraction_url_lat_lng(url):
    list_positions = url.split('search_type=user_map_move&')
    list_position_splitted = list_positions[1].split('&')
    print(list_position_splitted[0].split('=')[1])
    print(list_position_splitted[1].split('=')[1])
    print(list_position_splitted[2].split('=')[1])
    print(list_position_splitted[3].split('=')[1])




# EXAMPLE all_params

# lst = url.split('/')
#     print(lst)
#     query_param = lst[5].split('?')
#     print("---------------")
#     all_params = query_param[1].split('&')
#     print(all_params)


# [
#     'tab_id=home_tab',
#     'refinement_paths%5B%5D=%2Fhomes',
#     'flexible_trip_lengths%5B%5D=one_week',
#     'price_filter_input_type=0',
#     'query=Corso%20San%20Gottardo%2C%20Milano%2C%20MI',
#     'place_id=EiZDb3JzbyBTYW4gR290dGFyZG8sIE1pbGFubywgTUksIEl0YWxpYSIuKiwKFAoSCZdiDwkIxIZHEYwn8Av-7lFfEhQKEgnndRI_ScGGRxGNDnTGE83_PA',
#     'date_picker_type=calendar',
#     'source=structured_search_input_header',
#     'search_type=user_map_move',
#     'ne_lat=45.45175336428956',
#     'ne_lng=9.184378460246307',
#     'sw_lat=45.441335890121145',
#     'sw_lng=9.169808700877411',
#     'zoom=16',
#     'search_by_map=true'
# ]
