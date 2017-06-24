import json
import os
import sys
from MarketData.GDAXMarketData import GDAXMarketData

class GDAXMarketDataMock(GDAXMarketData):
    """Mock for market data"""

    def __init__(self, start, end, granularity, product, isCreatingData = False):
        self.isCreatingData = isCreatingData        
        self.testDir = os.path.dirname(os.path.abspath(__file__))
        self.cannedDataDir = os.path.join(self.testDir, '../CannedData')
        self.mockDataTestPath = os.path.join(self.cannedDataDir, 'MockData.json')
        
        with open(self.mockDataTestPath, 'r') as fp:
            self.mockData = json.load(fp)

        self.timeseries = self.BuildTimeSeries(start, end, granularity, product)
        
    def BuildTimeSeries(self, start, end, granularity, product):
        key = '{}{}{}{}'.format(start, end, granularity, product)

        if (self.isCreatingData):
            timeSeries = super(GDAXMarketDataMock, self).BuildTimeSeries(start, end, granularity, product)            
            self.mockData[key] = timeSeries
            with open(self.mockDataTestPath, 'w') as fp:
                json.dump(self.mockData, fp)

        return self.mockData[key]           
    
    def GetNextCandle(self):
        candleSticks = sorted(self.timeseries.items())
        for key, candleStick in candleSticks:
            yield candleStick