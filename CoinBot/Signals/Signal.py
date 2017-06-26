""" Base Module for Signals """

class Signal(object):
    """Interace for classes to define a signal"""

    def add_new_candle_stick(self, candle_stick):
        """ Adds a new candle stick for the signal to interpret """
        pass

    def get_market_signal(self):
        """ Get the current signal value """
        pass
