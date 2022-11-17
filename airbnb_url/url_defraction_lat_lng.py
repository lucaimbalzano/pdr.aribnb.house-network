# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

list_NWSE = []

def checkin_checkout_link_assembly(checkin_input, checkout_input):
    link_part_zoom_and_map_mode_search = '&zoom=16&search_by_map=true&'
    
    checkin = 'checkin='+checkin_input
    checkout = '&checkout='+checkout_input
    return link_part_zoom_and_map_mode_search + checkin + checkout_input


def moving_map_nwse_calculation(url, list_lat_lng, MOVETO_VALUES_NWSE, checkin_input, checkout_input):
    ne_lat = 0;
    ne_lng = 0;
    sw_lat = 0;
    sw_lng = 0;
    
# MOVETO_VALUES_NWSE (in Debug) 
#       0               1                   2               3               4
# [[1, 1, 1, 1], 0.00973053189324, 0.0031328199521, 0.00971727625327, 0.003132819952099]

    if(MOVETO_VALUES_NWSE[0][0] == 0):
        ne_lat = float(list_lat_lng[0].split('=')[1]) - MOVETO_VALUES_NWSE[1]
    else:
        ne_lat = float(list_lat_lng[0].split('=')[1]) + MOVETO_VALUES_NWSE[1]
    
    if(MOVETO_VALUES_NWSE[0][1] == 0):
        ne_lng = float(list_lat_lng[1].split('=')[1]) - MOVETO_VALUES_NWSE[2]
    else:   
        ne_lng = float(list_lat_lng[1].split('=')[1]) + MOVETO_VALUES_NWSE[2]

    if(MOVETO_VALUES_NWSE[0][2] == 0):
        sw_lat = float(list_lat_lng[2].split('=')[1]) - MOVETO_VALUES_NWSE[3]
    else:   
        sw_lat = float(list_lat_lng[2].split('=')[1]) + MOVETO_VALUES_NWSE[3]
    
    if(MOVETO_VALUES_NWSE[0][3] == 0):
        sw_lng = float(list_lat_lng[3].split('=')[1]) - MOVETO_VALUES_NWSE[4]
    else:   
        sw_lng = float(list_lat_lng[3].split('=')[1]) + MOVETO_VALUES_NWSE[4]
   
    # this is without checkin&checkout
    # list_whole = url.split('search_type=user_map_move&')
    list_whole = url.split('filter_change&')

    url_defined = list_whole[0] + 'ne_lat=' + str(ne_lat) + '&ne_lng=' + str(ne_lng) + '&sw_lat=' + str(sw_lat) + '&sw_lng=' + str(sw_lng)
    return url_defined + checkin_checkout_link_assembly(checkin_input, checkout_input);
    

def defraction_url_lat_lng(url, search_type):
    # search_type=search_query&
    # search_type=user_map_move&
    list_positions = url.split(search_type)
    list_position_splitted = list_positions[1].split('&')
    return list_position_splitted
