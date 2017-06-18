
import GDAX
import pprint
import time
import datetime
from GDAXHistorical import GDAXHistorical
from Signals.MomentumSignal import MomentumSignal
from Signals.TypeMarketSignal import TypeMarketSignal

def main():
     
  now = time.strftime("%c")
  print("High I am CoinBot.  Current time %s"  % now)
  print('')
  printCurrentState()  

  historical = GDAXHistorical()
  timeSeries = historical.BuildTimeSeries(datetime.datetime(2017, 1, 11, 0, 0), datetime.datetime(2017, 6, 14, 0, 0), 3000, 'ETH-USD')

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
  pointItems = sorted(timeSeries.items())
  pointList = list(pointItems)
  firstPoint = pointItems[0][1]
  
  for key, point in pointItems:
      if cnt % 20 == 0:
          printRow('TotalValue', [ 'Gain', 'BenchmarkGain', 'Gain %', 'Benchmark Gain %', 'Diff %', 'Price'])      
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

def printCurrentState():  
  printRow('Product', getStats().keys())
  products = {'ETH-USD', 'BTC-USD', 'LTC-USD'}    
  for product in products:        
    printRow(product, getStats(product).values())

def getStats(product='BTC-USD'):
    publicClient = GDAX.PublicClient(product_id=product)
    return publicClient.getProduct24HrStats()              

def printRow(key, values):
    row_format = "{:>17}" * (len(values) + 1)
    print(row_format.format(key, *values))      

if __name__ == "__main__":
    main() 
 