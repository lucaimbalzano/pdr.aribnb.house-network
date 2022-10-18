

import datetime
from dto.checkin_checkout import Checkin_checkout


class InputConsole:
  check_inout_list = []
  checkin_checkout = Checkin_checkout(datetime.date.today(),datetime.date.today())
  check_inout_list.append(checkin_checkout)
  def __init__(self,address,check_inout_list,adults, lat, lng):
    self.name = address
    self.check_inout_list = check_inout_list
    self.adults = adults
    self.lat = lat
    self.lng = lng

  # InputConsole(address, check_inout_list, adults, lat, lng)

  def __setattr__(self, address: str, check_inout_list: [], adults: int, lat: int, lng: int) -> None:
    super().__setattr__(address, check_inout_list, adults, lat, lng)