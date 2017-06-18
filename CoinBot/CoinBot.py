
import GDAX
import pprint
import time
import datetime

def main():
    now = time.strftime("%c")
    print("High I am CoinBot.  Current time %s"  % now)
    print('')
    printCurrentState()  

def getStats(product='BTC-USD'):
    publicClient = GDAX.PublicClient(product_id=product)
    return publicClient.getProduct24HrStats()              

if __name__ == "__main__":
    main() 
 