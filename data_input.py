import requests

class Parse:

    def __init__(self, coin1 = 'ltc', coin2 = 'usdt', limit = 150):
        self.coin_bs = coin1
        responce = requests.get(url=f'https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1')

        total_trade_ask = 0
        total_trade_bit = 0

        for item in responce.json()[f'{coin1}_usdt']:
            if item['type'] == 'ask':
                total_trade_ask += item['price'] * item['amount']
            if item['type'] == 'bid':
                total_trade_bit += item['price'] * item['amount']

        self.total_trade_ask = total_trade_ask
        self.total_trade_bit = total_trade_bit

        total_trades = total_trade_ask + total_trade_bit # сумма ордеров на покупку и продажу
        self.total_trades = total_trades

        responce_avg_price = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}?&ignore_invalid=1')
        avg_price = responce_avg_price.json()[f'{coin1}_{coin2}']['avg']
        self.avg_price = avg_price

    def trade_ask(self):
        proc_ask = self.total_trade_ask / self.total_trades # сколько процентов на продажу от общего количества
        return proc_ask

    def trade_bid(self):
        proc_bid = self.total_trade_bit / self.total_trades # сколько процентов на покупку от общего кол - ва
        return proc_bid

    def total_summer(self): # сумма ордеров на покупку и продажу
        return self.total_trades

    def inf_price(self): # средняя цена
        return self.avg_price

class Recomendation(Parse):

    def rec_price(self):
        proc_bid = self.total_trade_bit / self.total_trades
        otklonenie = proc_bid - 0.5 # насколько ордеров на покупку в прцоентах больше 50 %.
        otklonenie = 1 + otklonenie
        recommended_price = self.avg_price * otklonenie
        self.recommended_price = recommended_price
        return recommended_price

    def coin_nm(self):
        return self.coin_bs

    def buy(self):
        if self.recommended_price > self.avg_price:
            return 'buy'
        else:
            return 'don-t buy'

