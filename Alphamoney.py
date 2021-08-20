class MoneyFmt:
  def init(self, value = 0.0):
    self.value = float(value)
  def update(self, value = None):
    self.value = value
  def str(self):
    if self.value >= 0:
      return '${:,.2f}'.format(self.value)
    else:
      return '-${:,.2f}'.format(-self.value)
  def repr(self):
    print(self.value)
    return f'{self.value}'

cash = MoneyFmt()