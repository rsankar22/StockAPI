from yahoo_fin import stock_info
import pandas as pd
import plotly.offline
from plotly.offline import plot,init_notebook_mode
init_notebook_mode()
import cufflinks as cf
from datetime import date
cf.set_config_file(offline=True)
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
def pullLiveVisual():
    check = 'Y'
    while check == 'Y':
        user_pull = input('What stock would you like to analyze?')
        stock_info.get_live_price(user_pull)
        curr_date = date.today()
        df = stock_info.get_data(user_pull, start_date='01/01/2019', end_date = curr_date)
        qf = cf.QuantFig(df)
        qf.add_bollinger_bands()
        qf.add_macd()
        qf.iplot(kind = 'ohlc', asPlot=True)

        check = input('Continue? [Y/N]: ')


def pullLiveData():
    check = 'Y'
    while check == 'Y':
        user_pull = input('What stock would you like to analyze?')
        stock_info.get_live_price(user_pull)
        curr_date = date.today()
        df = stock_info.get_data(user_pull, start_date='01/01/2019', end_date=curr_date)
        qf = cf.QuantFig(df)
        qf.add_bollinger_bands()
        qf.add_macd()
        qf.iplot(kind='ohlc', asFrame=True)

        check = input('Continue? [Y/N]: ')
