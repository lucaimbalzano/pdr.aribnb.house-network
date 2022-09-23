# coding=utf-8
from airbnb_scraping.airbnb_extraction import core_extraction
from cronometer import ChronoMeter
import datetime as dt
import time

VERSION = 'V1.001'
link = 'https://www.airbnb.it/'

if __name__ == '__main__':
    print(VERSION+" : Airbnb - Pdr Started:")
    print("## started cycle - inside loop ##")
    chrono = ChronoMeter()
    chrono.start_chrono()

    core_extraction()

    # while True:
    #     for i in (1, 10):
    #         print("## started cycle - inside loop ##")
    #         ora = dt.datetime.now().time().hour
    #         minuti = dt.datetime.now().time().minute
    #
    #
    #         # login()
    #
    #
    #     chrono.stop_chrono()
    #     chrono.print_time()
    #     print("## finished cycle - exit ##")
    exit(1)
