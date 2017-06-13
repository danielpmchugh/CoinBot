
import GDAX
import pprint
import time
import datetime
from GDAXHistorical import GDAXHistorical

def main():
     
  now = time.strftime("%c")
  print("High I am CoinBot.  Current time %s"  % now)
  print('')
  printCurrentState()  

  historical = GDAXHistorical()
  timeSeries = historical.BuildTimeSeries(datetime.datetime(2017, 1, 1, 0, 0), datetime.datetime(2017, 6, 11, 0, 0), 3000, 'ETH-USD')

def printCurrentState():  
  printRow('Product', getStats().keys())
  products = {'ETH-USD', 'BTC-USD', 'LTC-USD'}    
  for product in products:        
    printRow(product, getStats(product).values())

def getStats(product='BTC-USD'):
    publicClient = GDAX.PublicClient(product_id=product)
    return publicClient.getProduct24HrStats()              

def printRow(key, values):
    row_format = "{:>15}" * len(values)
    print(row_format.format(key, *values))      

if __name__ == "__main__":
    main() 
