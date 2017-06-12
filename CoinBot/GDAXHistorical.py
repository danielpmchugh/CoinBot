import GDAX
from datetime import timedelta

class GDAXHistorical(object):
  """Class will contain function to query historical data from GDAX"""
  
  def BuildTimeSeries(self, start, end, granularity, product='BTC-USD'):
    print("Building time series with granuality of %s seconds. Starting %s and ending %s" % (granularity, start, end))
    
    publicClient = GDAX.PublicClient(product_id=product)

    #gdax must break call out by 200 candles/groups

    historicalRates = []
    maxCandles = 200
    windowStart = start
    while (windowStart < end):
        windowEnd = windowStart + timedelta(seconds=granularity * (maxCandles-1))
        if windowEnd > end:
            windowEnd = end
        print("Requesting candles between %s and %s" % (windowStart, windowEnd))
        windowHistoricalRates = publicClient.getProductHistoricRates(granularity=granularity, start=windowStart, end=windowEnd)
        historicalRates.extend(windowHistoricalRates)
        windowStart += timedelta(0, granularity * maxCandles)

        