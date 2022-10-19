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
    if isinstance(current_date, Checkin_checkout):
        day = datetime.datetime.strptime(str(current_date.date_checkout), '%Y-%m-%d').weekday()
    else:
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

    logger.debug('[DEBUG] day: '+ day_name[day]+', stays until friday = '+str(stays))
    return stays


def get_stays_missing_last_monday(current_date):
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if isinstance(current_date, Checkin_checkout):
        day = datetime.datetime.strptime(str(current_date.date_checkout), '%Y-%m-%d').weekday()
    else:
        day = datetime.datetime.strptime(current_date, '%Y-%m-%d').weekday()
    stays = 0

    if(day_name[day] == 'Monday'):
        stays = 0
    if(day_name[day] == 'Tuesday'):
        stays = 1
    if (day_name[day] == 'Wednesday'):
        stays = 2
    if (day_name[day] == 'Thursday'):
        stays = 3
    if (day_name[day] == 'Friday'):
        stays = 4
    if (day_name[day] == 'Saturday'):
        stays = 5
    if (day_name[day] == 'Sunday'):
        stays = 6

    logger.debug('[DEBUG] day: '+ day_name[day]+', stays until last monday = '+str(stays))
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
    if isinstance(date_param, Checkin_checkout):
        data_checkin_date = get_date_data_by_str(get_clean_date_by_str(str(date_param.date_checkout)))
    else:
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




def get_checkin_checkout_WEEK_numM(current_date, stays):
    stays_until_friday = get_stays_missing_until_friday(current_date)

    begin_date_from_friday = get_range_time_stays(current_date,stays_until_friday).date_checkout
    stays = stays -1
    checkin_checkout = get_range_time_stays(begin_date_from_friday,stays)
    return checkin_checkout;


def get_checkin_checkout_INFRA_numM(current_date, stays):
    stays_until_monday = get_stays_missing_last_monday(current_date)
    begin_date_from_monday = get_range_time_stays(current_date, -stays_until_monday).date_checkout
    checkin_checkout = get_range_time_stays(begin_date_from_monday, stays)
    return checkin_checkout



def get_check_inout_list(stays):
    today = datetime.date.today()

    today_plus_month = get_range_time_stays(datetime.date.today(),30)
    checkin_checkout1M = get_range_time_stays(today_plus_month.date_checkout, stays)
    checkin_checkout1M_INFRA = get_checkin_checkout_INFRA_numM(checkin_checkout1M.date_checkin, stays)
    checkin_checkout1M_WEEK = get_checkin_checkout_WEEK_numM(checkin_checkout1M_INFRA.date_checkout, stays)

    today_plus_3month = get_range_time_by_stays_and_stays_3MONTH(str(today),stays)
    checkin_checkout3M = get_range_time_stays(today_plus_3month.date_checkout, stays)
    checkin_checkout3M_INFRA = get_checkin_checkout_INFRA_numM(checkin_checkout3M.date_checkin, stays)
    checkin_checkout3M_WEEK = get_checkin_checkout_WEEK_numM(checkin_checkout3M_INFRA.date_checkout, stays)

    today_plus_6month = get_range_time_by_stays_and_stays_6MONTH(str(today), stays)
    checkin_checkout6M = get_range_time_stays(today_plus_6month.date_checkout, stays)
    checkin_checkout6M_INFRA = get_checkin_checkout_INFRA_numM(checkin_checkout6M.date_checkin, stays)
    checkin_checkout6M_WEEK = get_checkin_checkout_WEEK_numM(checkin_checkout6M_INFRA.date_checkout, stays)


    check_inout_list = [checkin_checkout1M_INFRA,checkin_checkout1M_WEEK,
                        checkin_checkout3M_INFRA, checkin_checkout3M_WEEK,
                        checkin_checkout6M_INFRA, checkin_checkout6M_WEEK]

    return check_inout_list



def get_last_day_of_the_month(currentDate):
     return datetime.date(currentDate.year, currentDate.month,
                         calendar.monthrange(currentDate.year, currentDate.month)[1])




