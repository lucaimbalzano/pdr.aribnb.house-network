import calendar
import datetime
from cgi import test
from datetime import date

from settings.settings_date import JAN_len, FEB_len, MAR_len, APR_len, \
    MAY_len, JUN_len, JUL_len, AUG_len, SEP_len, NOV_len, OCT_len, DEC_len


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
