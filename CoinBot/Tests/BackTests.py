import unittest
import time
import datetime
from MarketData.GDAXMarketData import GDAXMarketData
from Tests.Mock.GDAXMarketDataMock import GDAXMarketDataMock
from Signals.MomentumSignal import MomentumSignal
from Signals.TypeMarketSignal import TypeMarketSignal
from Models.Portfolio import Portfolio
from Utilities.StatusUtility import StatusUtility

class Test_BackTests(unittest.TestCase):
    def test_backtest(self):

        marketData = GDAXMarketDataMock(datetime.datetime(2017, 1, 11, 0, 0), datetime.datetime(2017, 6, 14, 0, 0), 3000, 'ETH-USD', False)
        
        momentumSignal = MomentumSignal()
  
        tradeIncrements = {
            TypeMarketSignal.StrongBuy : 2,
            TypeMarketSignal.Buy: 1,
            TypeMarketSignal.Neutral: 0,
            TypeMarketSignal.Sell: -1,
            TypeMarketSignal.StrongSell: -2}

        start = 100
        wallet = start
        position = 0
    
        portfolio = Portfolio(start)
        benchmark = Portfolio(start)
        cnt = 0
        
        firstPoint = None
  
        for point in marketData.GetNextCandle():                    
            if firstPoint == None:
                # Benchmark is fully allocated to ETC
                benchmark.adjustCash(start * -1)
                benchmark.adjustEtc(start / point['close'])

            #   TODO: Process Signals
            momentumSignal.AddNewCandleStick(point)
            
            #   TODO: Analyzer Read Signals / output confidence matrix

            #   TODO: Strategy Read confidence matrix and return exectuion instructions
            tradeIncrement = tradeIncrements[momentumSignal.GetMarketSignal()]      
            if tradeIncrement + position < 0:
                tradeIncrement = 0
          
            #   TODO: Executor Update portfolio composition 
            cost = tradeIncrement * point['close']
            if cost > wallet:
                tradeIncrement = 0
                cost = 0
                print("No More money :(.")          
            
            benchmark.etcPx = point['close']
            portfolio.etcPx = point['close']
            portfolio.adjustCash(cost * -1)
            portfolio.adjustEtc(tradeIncrement)
            
            StatusUtility.print(portfolio, benchmark)                    

if __name__ == '__main__':
    unittest.main()