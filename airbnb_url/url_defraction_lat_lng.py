from main import settings


list_NWSE = []

def moving_to_nord_calculation(url,list_lat_lng):
    ne_lat = float(list_lat_lng[0].split('=')[1])+ settings.NORD_NE_LAT
    ne_lng = float(list_lat_lng[1].split('=')[1])+ settings.NORD_NE_LNG
    sw_lat = float(list_lat_lng[2].split('=')[1])+ settings.NORD_SW_LAT
    sw_lng = float(list_lat_lng[3].split('=')[1])+ settings.NORD_SW_LNG
    list_whole = url.split('search_type=user_map_move&')
    url_defined = list_whole[0] + 'ne_lat=' + str(ne_lat) + '&ne_lng=' + str(ne_lng) + '&sw_lat=' + str(sw_lat) + '&sw_lng=' + str(sw_lng)
    return url_defined;

def moving_map_nwse_calculation(url, list_lat_lng, MOVETO_VALUES_NWSE):
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
   
    list_whole = url.split('search_type=user_map_move&')
    url_defined = list_whole[0] + 'ne_lat=' + str(ne_lat) + '&ne_lng=' + str(ne_lng) + '&sw_lat=' + str(sw_lat) + '&sw_lng=' + str(sw_lng)
    return url_defined;
    

def defraction_url_lat_lng(url):
    list_positions = url.split('search_type=user_map_move&')
    list_position_splitted = list_positions[1].split('&')
    return list_position_splitted
