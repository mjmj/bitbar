#!/usr/bin/env -S PATH="${PATH}:/usr/local/bin" PYTHONIOENCODING=UTF-8 LC_ALL=en_US.UTF-8 python3
# coding=utf-8

########################
# Bitbar Bitcoin ticker
########################

import json
from urllib.request import urlopen

API_KEY = ''

CURRENCY = 'BTC'
EXCHANGE = 'gdax'
QUOTE = 'USD'

DAYS = '1d'
MARKET_URL = 'https://api.nomics.com/v1/currencies/ticker?key={}&interval={}d'.format(API_KEY, DAYS)
TA_URL = 'https://www.tradingview.com/chart/h1lG576p/'


def get_price_change(coin, days):
    response = json.loads(urlopen(MARKET_URL).read().decode('utf-8'))
    for item in response:
        if item.get('currency') == coin:
            change = item.get(days)['price_change_pct']

    return float(change)

def main():
    MARKET_PRICES = ''

    URL = "https://api.nomics.com/v1/exchange-markets/prices?key={}&currency={}&exchange={}".format(API_KEY, CURRENCY, EXCHANGE)
    response = urlopen(URL).read()
    content = json.loads(response.decode('utf-8'))

    for c in content:
        if c.get('quote') == QUOTE:
            change = get_price_change(CURRENCY, DAYS)

            if change > float(0):
                image = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QAyQACAALwzISXAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACkSBTjB+AAAALNJREFUOMvVk70NAjEMhb87WYiGBZAQU7ABNSVSWpZgEEagsJDoKBELUCEKFuBuCKTw0xyQC0lICe5i+/k9/wT+3opUUJQhcAUqa8I5ZQT4tANwioGTCkQZA9vmOQE2oUJFhL0DXBz33RpKUfCLfLTQJMx9IlEWuQr6QB3prGtNS1lwiMvEYo7ekNsKRBkB+y+rH1hDFVOwy7ids+gbVzrsM6CXeYDTF85xroB1ZoHb73ymB5RhJkpZTihGAAAAAElFTkSuQmCC color=#000000'
            else:
                image = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QABACnAADQ9FZaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACQ1FZwK3gAAAMRJREFUOMvNkjEKAjEQRZ+jKNjYKh5AbzCdjVcQj+BFPIKlp7EMeAJrUbASQVCEr80uG9cNbqe/Cgn/5WUI/DqNfBHM+kCzbs+lPUAr2pwBq5qABbB+M8gszkDvS/kOdAG5VBgEM4ApsP0CGLukjxlEoA0wSZR3Lo0qhxhZDIBDAmDA0wsBLD51CZeOwLKivHbprZx6AkAHuEXbD5fawYwywMqAzOKeDTTPvKqcTGZBMLsGs0utn5gADYEHcKp9e9ni//MCDtNCE3qjsIwAAAAASUVORK5CYII= color=#000000'

            percent_change =  "(" + "{:0.2f}".format(change * 100) + "%)"
            price = float(c.get('price_quote'))

            print('%s %.2f %s | image=%s href=%s' % (CURRENCY, price, percent_change, image, TA_URL))

main()
