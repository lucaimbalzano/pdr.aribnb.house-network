# Dreams without Goals are just Dreams
#
# - @lucaimbalzano



import datetime
from dto.checkin_checkout import Checkin_checkout


class InputConsole:
  def __init__(self, address, check_inout_list, adults, lat, lng):
    self.address = address
    self.check_inout_list = check_inout_list
    self.adults = adults
    self.lat = lat
    self.lng = lng