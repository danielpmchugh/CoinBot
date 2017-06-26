""" Base Module for Momentum Signals """

from Signals.Signal import Signal

class MomentumSignal(Signal):
    """ Module to signal when ther eis buy or sell momentum """
    def __init__(self):
        super(MomentumSignal, self).__init__()
        self.momentum = 0
        self.previous_price = 0

    def add_new_candle_stick(self, candle_stick):
        """ Add new candlestick to signal analysis """
        if self.previous_price != 0:
            if self.previous_price < candle_stick['close'] and self.momentum < 1:
                self.momentum = self.momentum + 1
            if self.previous_price > candle_stick['close'] and self.momentum > -1:
                self.momentum = self.momentum - 1
        self.previous_price = candle_stick['close']

    def get_market_signal(self):
        """ Get Market Signal """
        if self.momentum == -2:
            return -1
        if self.momentum == -1:
            return -.5
        if self.momentum == -0:
            return 0
        if self.momentum == 1:
            return .5
        if self.momentum == 2:
            return 1
