import unittest
import time
import datetime
from MarketData.GDAXMarketData import GDAXMarketData
from Tests.Mock.GDAXMarketDataMock import GDAXMarketDataMock
from Signals.MomentumSignal import MomentumSignal
from Signals.TypeMarketSignal import TypeMarketSignal


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
    
        cnt = 0
        
        firstPoint = None
  
        for point in marketData.GetNextCandle():                    
            if firstPoint == None:
               firstPoint = point
            #   TODO: Process Signals
            #   TODO: Analyzer Read Signals / output confidence matrix
            #   TODO: Strategy Read confidence matrix and return exectuion instructions
            if cnt % 20 == 0:
                self.printRow('TotalValue', [ 'Gain', 'BenchmarkGain', 'Gain %', 'Benchmark Gain %', 'Diff %', 'Price'])      
            cnt = cnt + 1
            momentumSignal.AddNewCandleStick(point)
            tradeIncrement = tradeIncrements[momentumSignal.GetMarketSignal()]      
            if tradeIncrement + position < 0:
                tradeIncrement = 0
          
            cost = tradeIncrement * point['close']
            if cost > wallet:
                tradeIncrement = 0
                cost = 0
                print("No More money :(.")          

            wallet = wallet - cost
            position = position + tradeIncrement      
            unrealizedGains = position * point['close']
            totalvalue = wallet + unrealizedGains
            gain = totalvalue - start
            gainPct = gain / start
            benchmarkTotalValue = (start / firstPoint['close']) * point['close']
            benchmarkGain = benchmarkTotalValue - start
            benchmarkGainPct = benchmarkGain/ start
            diffPct = gainPct - benchmarkGainPct 
            print('{:>17}{:>17}{:>17}{:>17}{:>17}{:>17}{:>17}'.format(
                '{0:.2f}'.format(totalvalue), 
                '{0:.2f}'.format(gain),
                '{0:.2f}'.format(benchmarkGain),
                '{0:.2f}'.format(gainPct),          
                '{0:.2f}'.format(benchmarkGainPct),          
                '{0:.2f}'.format(diffPct),
                '{0:.2f}'.format(point['close'])))            
        
            
    def printRow(self, key, values):
        row_format = "{:>17}" * (len(values) + 1)
        print(row_format.format(key, *values))      

if __name__ == '__main__':
    unittest.main()