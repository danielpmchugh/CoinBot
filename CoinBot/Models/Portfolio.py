class Portfolio(object):
    def __init__(self, cash):
        self._cash = cash
        self._initialValue = cash
        self._etcQty = 0
        self._btcQty = 0
        self._ltcQty = 0
        self._etcPx = 0
        self._btcPx = 0
        self._ltcPx = 0        

    def get_etcPx(self):
        return self._etcPx

    def set_etcPx(self, value):
        self._etcPx = value
            
    def get_btcPx(self):
        return self._btcPx

    def set_btcPx(self, value):
        self._btcPx = value

    def get_ltcPx(self):
        return self._ltcPx

    def set_ltcPx(self, value):
        self._ltcPx = value

    etcPx = property(get_etcPx, set_etcPx)
    btcPx = property(get_btcPx, set_btcPx)
    ltcPx = property(get_ltcPx, set_ltcPx)    

    def adjustCash(self, amount):
        self._cash = self.cash + amount

    def adjustEtc(self, quantity):
        self._etcQty = self._etcQty + quantity


    @property
    def unrealizedGains(self):
        return self._etcQty * self._etcPx + self._btcQty * self._btcPx + self._ltcQty * self._ltcPx

    @property
    def cash(self):
        return self._cash

    @property
    def currentValue(self):
        return self.cash + self.unrealizedGains

    @property
    def returns(self):
        return self.currentValue - self._initialValue

    @property
    def yieldPct(self):
        return self.returns / self._initialValue