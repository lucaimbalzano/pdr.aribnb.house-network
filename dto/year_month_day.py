# Dreams without Goals are just Dreams
#
# - @lucaimbalzano



class Year_Month_Day:
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

  def __setattr__(self, year: int, month: int, day: int) -> None:
    super().__setattr__(year, month, day)
  #
  # def __setattr__(self, year: str, month: str, day: str) -> None:
  #   super().__setattr__(year, month, day)
