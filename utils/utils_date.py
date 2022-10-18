# coding=utf-8
# Dreams without Goals are just Dreams
#
# - @lucaimbalzano

import calendar
import calendar
from dto.calendar_filled import get_calendar_filled
from dto.checkin_checkout import Checkin_checkout
from datetime import datetime
from datetime import timedelta
from datetime import date
import datetime
import time


def get_range_time_stays(date_param, stays):
    begin_date_checkin_string = str(date_param)
    print("utils_dateget_range_time_stays(date_param,stays)"+str(date_param))
    checkin = datetime.datetime.strptime(begin_date_checkin_string, "%Y-%m-%d")
    # checkin = datetime.strptime(begin_date_checkin_string, "%Y-%m-%d")
    checkout = checkin + timedelta(days=stays)
    return Checkin_checkout(checkin, checkout)

def get_range_time_by_stays_and_stays_3MONTH(date_param, stays):
    stays = 90 + stays
    checkin_checkout = get_range_time_stays(date_param, stays)
    return checkin_checkout


def get_range_time_by_stays_and_stays_6MONTH(date_param, stays):
    stays = 180 + stays
    return get_range_time_stays(date_param, stays)



class Utils_date:

    def get_date_by_today():
        dates_checking_checkout_master = []
        dates_checkin_checkout = Checkin_checkout('2022-11-22', '2022-11-27')
        dates_checking_checkout_master.append(dates_checkin_checkout)
        dates_checkin_checkout = Checkin_checkout('2022-11-22', '2022-11-27')
        dates_checking_checkout_master.append(dates_checkin_checkout)
        dates_checkin_checkout = Checkin_checkout('2022-11-22', '2022-11-27')
        dates_checking_checkout_master.append(dates_checkin_checkout)

        date_checkin = '2022-11-22'
        date_checkout = '2022-11-27'


    def get_last_day_of_the_month(currentDate):
        return datetime.date(currentDate.year, currentDate.month,
                             calendar.monthrange(currentDate.year, currentDate.month)[1])


    def get_array_three_days_checkin_checkout(ymd_current, stays_days):
        checking_checkout = []
        checking_checkout = get_checkin_checkout_days()
        calendar = get_calendar_filled()
        if(ymd_current[2] < get_last_day_of_the_month(datetime.date.today())):
            for index_stays_days in range(1,get_last_day_of_the_month(datetime.date.today())):
                for index_month in range(1,13):
                    for index_day in range(1,):

                        return
                return

        return

    # def get_array_three_days_checkin_checkout(ymd_current, stays_days):
    #     checking_checkout = []
    #     checking_checkout = get_checkin_checkout_days()
    #     calendar = get_calendar_filled()
    #     for i in range (ymd_current[1],31):
    #         if(ymd_current[2] < get_last_day_of_the_month(datetime.date.today())):
    #             for index_stays_days in range(1,get_last_day_of_the_month(datetime.date.today())):
    #                 for index_month in range(1,13):
    #                     for index_day in range(1,):
    #
    #                         return
    #                 return
    #
    #         return



    def get_checkin_checkout_days():
        today = datetime.date.today()
        today_splitted_by_dash = str(today).split('-')
        checkout = int(today_splitted_by_dash[2]) + 2
        return Checkin_checkout(int(today_splitted_by_dash[2]), checkout)


    def get_today_splitted_int():
        today = datetime.date.today()
        today_splitted_by_dash = str(today).split('-')
        y = int(today_splitted_by_dash[0])
        m = int(today_splitted_by_dash[1])
        d = int(today_splitted_by_dash[2])
        ymd_list = []
        ymd_list.append(y)
        ymd_list.append(m)
        ymd_list.append(d)
        return ymd_list

    def get_day_splitted_int(string_date_param):
        today_splitted_by_dash = str(string_date_param).split('-')
        y = int(today_splitted_by_dash[0])
        m = int(today_splitted_by_dash[1])
        d = int(today_splitted_by_dash[2])
        ymd_list = []
        ymd_list.append(y)
        ymd_list.append(m)
        ymd_list.append(d)
        return ymd_list


    # def get_today_splitted_str():
    #     today = date.today()
    #     today_splitted_by_dash = str(today).split('-')
    #     ymd = Year_Month_Day(str(today_splitted_by_dash[0]), str(today_splitted_by_dash[1]), str(today_splitted_by_dash[2]))
    #     return ymd









