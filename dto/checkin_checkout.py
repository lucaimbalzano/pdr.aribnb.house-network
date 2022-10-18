# Dreams without Goals are just Dreams
#
# - @lucaimbalzano



from typing import Any


class Checkin_checkout:
  def __init__(self,date_checkin, date_checkout):
    self.date_checking = date_checkin
    self.date_checkout = date_checkout


  def __setattr__(self, date_checkin: str, date_checkout: str) -> None:
    super().__setattr__(date_checkin, date_checkout)