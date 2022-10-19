import calendar
import datetime
from cgi import test
from datetime import date

from settings.settings_date import JAN_len, FEB_len, MAR_len, APR_len, \
    MAY_len, JUN_len, JUL_len, AUG_len, SEP_len, NOV_len, OCT_len, DEC_len
from utils.utils_date import get_stays_missing_until_friday


@test
class TestDates:
    @test
    def test_get_between_week_by_month(self):
        today = date.today()
        today_splitted_by_dash = str(today).split('-')
        month = int(today_splitted_by_dash[1])

    @test
    def test_get_last_day_of_the_month(self):
        for i in range(1, 13):
            currentDate = i
            month = datetime.date(2022, currentDate,
                                  calendar.monthrange(2022, currentDate)[1])
            if (JAN_len or
                    FEB_len or
                    MAR_len or
                    APR_len or
                    MAY_len or
                    JUN_len or
                    JUL_len or
                    AUG_len or
                    SEP_len or
                    OCT_len or
                    NOV_len or
                    DEC_len == month):
                print(str(i) + ' - [DEBUG] test result: correct')
            else:
                print(str(i) + ' - [DEBUG] test result: wrong')

    @test
    def test_get_stays_missing_until_friday(self):
        date_current_m = '2022-10-17'
        date_current_t = '2022-10-18'
        date_current_w = '2022-10-19'
        date_current_th = '2022-10-20'
        date_current_fr = '2022-10-21'
        date_current_sat = '2022-10-22'
        date_current_sun = '2022-10-23'
        print('MONDAY')
        get_stays_missing_until_friday(date_current_m)
        print('TUESDAY')
        get_stays_missing_until_friday(date_current_t)
        print('WEDNESDAY')
        get_stays_missing_until_friday(date_current_w)
        print('THURSDAY')
        get_stays_missing_until_friday(date_current_th)
        print('FRIDAY')
        get_stays_missing_until_friday(date_current_fr)
        print('SATURDAY')
        get_stays_missing_until_friday(date_current_sat)
        print('SUNDAY')
        get_stays_missing_until_friday(date_current_sun)
