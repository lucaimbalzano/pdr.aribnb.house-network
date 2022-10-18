import settings.settings_date
from dto.month import Month


def get_calendar_filled():
    year_list = []
    month_list = []
    for i in range(1,365):
        for j in range(1, settings.settings_date.JAN_len):
                 month_list.append(Month('JAN', j))

        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.FEB_len):
                 month_list.append(Month('FEB', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.MAR_len):
                 month_list.append(Month('MAR', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.APR_len):
                 month_list.append(Month('APR', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.MAY_len):
                 month_list.append(Month('MAY', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.JUN_len):
                 month_list.append(Month('JUN', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.JUL_len):
                 month_list.append(Month('JUL', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.AUG_len):
                 month_list.append(Month('AUG', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.SEP_len):
                 month_list.append(Month('SEP', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.OCT_len):
                 month_list.append(Month('OCT', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.NOV_len):
                 month_list.append(Month('NOV', j))
        year_list.append(month_list)
        month_list = []
        for j in range(1,  settings.settings_date.DEC_len):
                 month_list.append(Month('DEC', j))
        year_list.append(month_list)
        return year_list


