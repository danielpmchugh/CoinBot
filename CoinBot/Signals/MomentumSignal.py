from Signals.Signal import Signal
from Signals.TypeMarketSignal import TypeMarketSignal

class MomentumSignal(Signal):
    def __init__(self):
        self.momentum = 0
        self.previous_price = 0

    def AddNewCandleStick(self, candleStick):
        if self.previous_price != 0:
            if (self.previous_price < candleStick['close'] and self.momentum < 1):
                self.momentum = self.momentum + 1
            if (self.previous_price > candleStick['close'] and self.momentum > -1):
                self.momentum = self.momentum - 1
        self.previous_price  = candleStick['close']
    
    def GetMarketSignal(self):
        if(self.momentum == -2):
            return TypeMarketSignal.StrongSell
        if(self.momentum == -1):
            return TypeMarketSignal.Sell
        if(self.momentum == -0):
            return TypeMarketSignal.Neutral
        if(self.momentum == 1):
            return TypeMarketSignal.Buy
        if(self.momentum == 2):
            return TypeMarketSignal.StrongBuy