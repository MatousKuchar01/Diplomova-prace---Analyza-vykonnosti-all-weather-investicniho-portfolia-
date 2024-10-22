import pandas as pd
import backtrader as bt

class AllWeatherStrategy(bt.Strategy):
    def __init__(self):
        # Definice jednotlivých aktiv v portfoliu
        self.stocks = self.datas[0]
        self.bonds = self.datas[1]
        self.gold = self.datas[2]

    def next(self):
        # Například nastavení váhování portfolia
        self.order_target_percent(self.stocks, target=0.3)
        self.order_target_percent(self.bonds, target=0.55)
        self.order_target_percent(self.gold, target=0.15)


def run_backtest()
    cerebro = bt.Cerebro()
    # Přidání dat pro aktiva (předpokládáme data uložená v CSV)
    cerebro.addData(bt.feeds.YahooFinanceCSVData(dataname='data/s&p500.csv'))
    cerebro.addData(bt.feeds.YahooFinanceCSVData(dataname='data/bonds.csv'))
    cerebro.addstrategy(AllWeatherStrategy)
    cerebro.run()
    cerebro.plot()

#Spuštění backtestu
run_backtest()
