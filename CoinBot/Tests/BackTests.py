""" Module for backtests """

import unittest
import datetime
from Tests.Mock.GDAXMarketDataMock import GDAXMarketDataMock
from Signals.MomentumSignal import MomentumSignal
from Models.Portfolio import Portfolio
from Utilities.StatusUtility import StatusUtility

class TestBackTests(unittest.TestCase):
    """ Back test class """
    @staticmethod
    def test_back_test():
        """ Method for backtesting """
        market_data = GDAXMarketDataMock(
            datetime.datetime(2017, 1, 11, 0, 0),
            datetime.datetime(2017, 6, 14, 0, 0),
            3000,
            'ETH-USD',
            False)

        momentum_signal = MomentumSignal()

        start = 100
        wallet = start
        position = 0

        portfolio = Portfolio(start)
        benchmark = Portfolio(start)
        first_point = None

        for point in market_data .get_next_candle():
            if first_point is None:
                # Benchmark is fully allocated to ETC
                first_point = point
                benchmark.adjust_cash(start * -1)
                benchmark.adjust_etc(start / first_point['close'])

            #   TODO: Process Signals
            momentum_signal.add_new_candle_stick(point)

            #   TODO: Analyzer Read Signals / output confidence matrix

            #   TODO: Strategy Read confidence matrix and return exectuion instructions
            trade_increment = momentum_signal.get_market_signal() * 2
            if trade_increment + position < 0:
                trade_increment = 0

            #   TODO: Executor Update portfolio composition
            cost = trade_increment * point['close']
            if cost > wallet:
                trade_increment = 0
                cost = 0
                print("No More money :(.")

            benchmark.etc_px = point['close']
            portfolio.etc_px = point['close']
            portfolio.adjust_cash(cost * -1)
            portfolio.adjust_etc(trade_increment)

            StatusUtility.print(portfolio, benchmark)

if __name__ == '__main__':
    unittest.main()
