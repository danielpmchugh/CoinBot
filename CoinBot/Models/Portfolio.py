""" Base Module for Portfolios """

class Portfolio(object):
    """ Module representing a portfolio """
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.

    def __init__(self, cash):
        self._cash = cash
        self._initial_value = cash
        self._etc_qty = 0
        self._btc_qty = 0
        self._ltc_qty = 0
        self._etc_px = 0
        self._btc_px = 0
        self._ltc_px = 0

    def get_etc_px(self):
        """ get current ethereum price """
        return self._etc_px

    def set_etc_px(self, value):
        """ set current ethereum price """
        self._etc_px = value

    def get_btc_px(self):
        """ get current bitcoin price """
        return self._btc_px

    def set_btc_px(self, value):
        """ set current bitcoin price """
        self._btc_px = value

    def get_ltc_px(self):
        """ get current litecoin price """
        return self._ltc_px

    def set_ltc_px(self, value):
        """ set current litecoin price """
        self._ltc_px = value

    etcPx = property(get_etc_px, set_etc_px)
    btcPx = property(get_btc_px, set_btc_px)
    ltcPx = property(get_ltc_px, set_ltc_px)

    def adjust_cash(self, amount):
        """ set current cash amount """
        self._cash = self.cash + amount

    def adjust_etc(self, quantity):
        """ set current ethereum amount """
        self._etc_qty = self._etc_qty + quantity

    @property
    def unrealized_gains(self):
        """ returns unrealized gains of the portfolio """
        etc_gains = self._etc_qty * self._etc_px
        btc_gains = self._btc_qty * self._btc_px
        ltc_gains = self._ltc_qty * self._ltc_px
        return  etc_gains + btc_gains + ltc_gains

    @property
    def cash(self):
        """ Get Cash value  """
        return self._cash

    @property
    def current_value(self):
        """ get current portfolio value """
        return self.cash + self.unrealized_gains

    @property
    def returns(self):
        """ get profit amount """
        return self.current_value - self._initial_value

    @property
    def yield_pct(self):
        """ get pct returned """
        return self.returns / self._initial_value
