import sys

def get_stock_price():
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
    rare_dict = {}
    arg = sys.argv[1].lower()

    for elem in COMPANIES:
        rare_dict[elem.lower()] = STOCKS[COMPANIES[elem]]

    if arg in rare_dict:
        print(rare_dict[arg])
    else:
        print('Unknown company')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_stock_price()
