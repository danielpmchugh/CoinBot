from interface import Interface

class Signal(Interface):
    """Interace for classes to define a signal"""

    def AddNewCandleStick(self, candleStick):
        pass

    def GetMarketSignal(self):
        pass


