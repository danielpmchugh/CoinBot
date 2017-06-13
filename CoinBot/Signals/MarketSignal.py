from enum import Enum

class MarketSignal(Enum):
    """Possible Market Signals"""
    StrongSell = 1
    Sell = 2
    Neutral = 3
    Buy = 4
    StrongBuy = 5


