"""This module Gets market data from GDAX"""

import time
from datetime import timedelta
import GDAX
from MarketData.MarketData import MarketData

class GDAXMarketData(MarketData):
    """Class will contain function to query historical data from GDAX"""

    # pylint: disable=too-few-public-methods
    # pylint: disable=no-self-use
    def build_time_series(self, start, end, granularity, product='BTC-USD'):
        """This function builds a time series from GDAX"""
        print("Building time series with granuality of %s seconds. Starting %s and ending %s"
              % (granularity, start, end))

        public_client = GDAX.PublicClient(product_id=product)

        #gdax must break call out by 200 candles/groups

        historical_rates = {}
        max_candles = 200
        window_start = start
        while window_start < end:
            window_end = window_start + timedelta(seconds=granularity * (max_candles-1))
            if window_end > end:
                window_end = end
            print("Requesting candles between %s and %s" % (window_start, window_end))
            window_historical_rates = public_client.getProductHistoricRates(
                granularity=granularity,
                start=window_start,
                end=window_end)
            time.sleep(1)
            window_historical_rates_dict = {
                int(k[0]): dict(zip(['low', 'high', 'open', 'close', 'volume'], k[1:]))
                for k in window_historical_rates}
            historical_rates.update(window_historical_rates_dict)
            window_start += timedelta(0, granularity * max_candles)
        return historical_rates

    def __init__(self):
        pass
