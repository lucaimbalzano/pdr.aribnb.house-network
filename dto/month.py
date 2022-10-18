


class Month:
  def __init__(self,name_month, days):
    self.name_month = name_month
    self.days = days

  def __setattr__(self, name_month: str, days: int) -> None:
    super().__setattr__(name_month, days)