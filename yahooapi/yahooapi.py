"""
I am mimicking Quantopian's get_pricing syntax

"""
from datetime import datetime, timedelta

import pandas as pd
from urllib import request
import json

LATEST_DATE = pd.datetime.today() - pd.tseries.offsets.BDay(1)



def get_stock_data(ticker, start_date, end_date):

    start_date = int(start_date.strftime("%s%f"))/1000000
    end_date = int(end_date.strftime("%s%f"))/1000000

    try:
        url = 'https://finance.yahoo.com/quote/%s/history?period1=%d&period2=%d&interval=1d&filter=history&frequency=1d' % (ticker, start_date, end_date)
        html = request.urlopen(url).read()
        price = html.split(b'"HistoricalPriceStore":{"prices":')[1].split(b',"isPending"')[0]
        return json.loads(price)
    except IndexError:
        raise IndexError('Ticker %s not found'%ticker )


def get_pricing(tickers, start_date='2006-1-1', end_date=LATEST_DATE, field='adjclose'):
    """

    :param tickers: one ticker or list of tickers
    :param start_date:
    :param end_date:
    :return:
    """

    if len(tickers) >5:
        raise ValueError('Too many tickers. Try below 5')

    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)
    if type(tickers) == list:
        dfs = []
        for t in tickers:
            data = get_stock_data(t, start_date, end_date)
            data = [d for d in data if not( 'type' in d)]
            dates = [datetime.fromtimestamp(d['date']).date() for d in data]
            data = pd.DataFrame(data, index=dates)[field]
            data.name = t
            dfs.append(data)

        return pd.concat(dfs, axis=1).sort_index(ascending = True)
    else:
        data = get_stock_data(tickers, start_date, end_date)
        data = [d for d in data if not ('type' in d)]
        dates = [datetime.fromtimestamp(d['date']) for d in data]
        data = pd.DataFrame(data, index=dates)[['adjclose', 'high', 'low', 'volume', 'close']]
        return data.sort_index(ascending = True)


