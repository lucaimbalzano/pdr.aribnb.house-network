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
from console.log.logger import get_logger



logger = get_logger()


def get_stays_missing_until_friday(current_date):
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = datetime.datetime.strptime(current_date, '%Y-%m-%d').weekday()
    stays = 0

    if(day_name[day] == 'Monday'):
        stays = 4
    if(day_name[day] == 'Tuesday'):
        stays = 3
    if (day_name[day] == 'Wednesday'):
        stays = 2
    if (day_name[day] == 'Thursday'):
        stays = 1
    if (day_name[day] == 'Saturday'):
        stays = -1
    if (day_name[day] == 'Sunday'):
        stays = -2
    print('[DEBUG] day: ' + day_name[day] + ', stays until friday = ' + str(stays))
    logger.debug('[DEBUG] day: '+ day_name[day]+', stays until friday = '+str(stays))
    return stays

def get_clean_date_by_str(date_str):
    date_splitted = date_str.split(' ')
    return date_splitted[0]

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


def get_date_data_by_str(data_str):
    ymd_checkin_int = get_day_splitted_int((get_clean_date_by_str(data_str)))
    data_date = datetime.date(ymd_checkin_int[0], ymd_checkin_int[1], ymd_checkin_int[2])
    return data_date


# def get_today_splitted_str():
#     today = date.today()
#     today_splitted_by_dash = str(today).split('-')
#     ymd = Year_Month_Day(str(today_splitted_by_dash[0]), str(today_splitted_by_dash[1]), str(today_splitted_by_dash[2]))
#     return ymd


def get_range_time_stays(date_param, stays):
    checkin = None
    checkout = None
    data_checkin_date = get_date_data_by_str(get_clean_date_by_str(str(date_param)))
    checkout = data_checkin_date + timedelta(days=stays)
    return Checkin_checkout(str(data_checkin_date), str(checkout))

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












