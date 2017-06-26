""" Module for status utility """

class StatusUtility(object):
    """ Status update utility class """
    @staticmethod
    def print(portfolio, benchmark, headers=False):
        """ Print the portfolio state """
        if headers:
            StatusUtility.print_header()
        print('{:>17}{:>17}{:>17}{:>17}{:>17}{:>17}{:>17}'.format(
            '{0:.2f}'.format(portfolio.current_value),
            '{0:.2f}'.format(portfolio.returns),
            '{0:.2f}'.format(benchmark.returns),
            '{0:.2f}'.format(portfolio.yield_pct),
            '{0:.2f}'.format(benchmark.yield_pct),
            '{0:.2f}'.format(portfolio.yield_pct - benchmark.yield_pct),
            '{0:.2f}'.format(benchmark.etc_px)))

    @staticmethod
    def print_header():
        """ Prints a header for the portfolio state """
        key = 'My Value'
        values = ['My Profit',
                  'Benchmark Profit',
                  'My Profit %',
                  'Benchmark Profit%',
                  'Diff %', 'Price']
        row_format = "{:>17}" * (len(values) + 1)
        print(row_format.format(key, *values))
