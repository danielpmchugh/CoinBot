""" Module for GDAX Market Data Mock """

import json
import os
from MarketData.GDAXMarketData import GDAXMarketData

class GDAXMarketDataMock(GDAXMarketData):
    """Mock for market data"""

    # pylint: disable=too-many-arguments
    # will com back to this

    def __init__(self, start, end, granularity, product, is_creating_data=False):
        super(GDAXMarketDataMock, self).__init__()
        self.is_creating_data = is_creating_data
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.canned_data_dir = os.path.join(self.test_dir, '../CannedData')
        self.mock_data_test_path = os.path.join(self.canned_data_dir, 'MockData.json')

        with open(self.mock_data_test_path, 'r') as file:
            self.mock_data = json.load(file)

        self.time_series = self.build_time_series(start, end, granularity, product)

    def build_time_series(self, start, end, granularity, product='BTC-USD'):
        key = '{}{}{}{}'.format(start, end, granularity, product)

        if self.is_creating_data:
            time_series = GDAXMarketData.build_time_series(
                start,
                end,
                granularity,
                product)
            self.mock_data[key] = time_series
            with open(self.mock_data_test_path, 'w') as file:
                json.dump(self.mock_data, file)

        return self.mock_data[key]

    def get_next_candle(self):
        """ Method to get next candle in timeseries """
        candle_sticks = sorted(self.time_series.items())
        for key, candle_stick in candle_sticks:
            yield candle_stick
