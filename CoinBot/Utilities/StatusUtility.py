class StatusUtility(object):
    @staticmethod
    def print(portfolio, benchmark, headers=False):            
        if headers:
            self.printRow('My Value', [ 'My Profit', 'Benchmark Profit', 'My Profit %', 'Benchmark Profit%', 'Diff %', 'Price'])      
        print('{:>17}{:>17}{:>17}{:>17}{:>17}{:>17}{:>17}'.format(
                '{0:.2f}'.format(portfolio.currentValue), 
                '{0:.2f}'.format(portfolio.returns),
                '{0:.2f}'.format(benchmark.returns),
                '{0:.2f}'.format(portfolio.yieldPct),          
                '{0:.2f}'.format(benchmark.yieldPct),          
                '{0:.2f}'.format(portfolio.yieldPct - benchmark.yieldPct),
                '{0:.2f}'.format(benchmark.etcPx)))            

    def printRow(self, key, values):
        row_format = "{:>17}" * (len(values) + 1)
        print(row_format.format(key, *values))      