import sys

def get_ticker_symbols():
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

    for elem in COMPANIES.items():
        rare_dict[elem[1].lower()] = [elem[0] , STOCKS[elem[1]]]

    if arg in rare_dict:
        print(*rare_dict[arg])
    else:
        print('Unknown company')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_ticker_symbols()