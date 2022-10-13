# coding=utf-8
from settings import settings
from airbnb_scraping.airbnb_extraction import core_extraction
from cronometer import ChronoMeter
import datetime as dt
import time
from airbnb_url import url_defraction_lat_lng

VERSION = 'V1.001'
# link = 'https://www.airbnb.it/'
link = 'https://www.airbnb.it/s/Corso-San-Gottardo--Milano--MI--Italia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&query=Corso%20San%20Gottardo%2C%20Milano%2C%20MI&place_id=EiZDb3JzbyBTYW4gR290dGFyZG8sIE1pbGFubywgTUksIEl0YWxpYSIuKiwKFAoSCZdiDwkIxIZHEYwn8Av-7lFfEhQKEgnndRI_ScGGRxGNDnTGE83_PA&date_picker_type=calendar&source=structured_search_input_header&search_type=user_map_move&ne_lat=45.45298769522644&ne_lng=9.185254798466218&sw_lat=45.44257044903232&sw_lng=9.170685039097322&zoom=16&search_by_map=true'

if __name__ == '__main__':
    print(VERSION+" : Airbnb -> PDR::Piano Di Rendimento")
    print("       : Airbnb -> AIP::Annual Income Plan")
    chrono = ChronoMeter()
    chrono.start_chrono()
    # core_extraction()

    list_position_splitted = url_defraction_lat_lng.defraction_url_lat_lng(link)
    url_moving_nord = url_defraction_lat_lng.moving_to_nord_calculation(link,list_position_splitted)
    print('MOVING INTO LINKS:')
    print('NORD: '+url_moving_nord)

    chrono.stop_chrono()
    chrono.print_time() 
    exit(1)

