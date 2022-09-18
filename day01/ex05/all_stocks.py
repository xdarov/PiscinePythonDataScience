import sys

class AllStocks:
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }
    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    def __init__(self) -> None:
        self.ticker_dict = {}
        self.price_dict = {}

        for elem in self.COMPANIES.items():
            self.ticker_dict[elem[1]] = [elem[1], elem[0]]
            self.price_dict[elem[0].upper()] = [elem[0], self.STOCKS[self.COMPANIES[elem[0]]]]


    def all_stocks(self, arg : str):
        # print(self.ticker_dict)
        # print(self.price_dict)
        if arg.upper() in self.ticker_dict:
            print(f"{self.ticker_dict[arg.upper()][0]} is a ticker symbol for {self.ticker_dict[arg.upper()][1]}")
        elif arg.upper() in self.price_dict:
            print(f"{self.price_dict[arg.upper()][0]} stock price is {self.price_dict[arg.upper()][1]}")
        else:
            print(f"{arg} is an unknown company or an unknown ticker symbol")


if __name__ == '__main__':
    obj = AllStocks()
    if (len(sys.argv) == 2):
        argv = sys.argv[1].replace(' ', '').split(',')
        for arg in argv:
            if arg != '':
                obj.all_stocks(arg)