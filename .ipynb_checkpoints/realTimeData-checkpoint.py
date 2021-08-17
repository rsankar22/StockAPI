from yahoo_fin import stock_info
import pandas as pd
import plotly.offline
from plotly.offline import init_notebook_mode
init_notebook_mode()
import cufflinks as cf
import matplotlib.pyplot as plt

cf.go_offline()
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
def pullLiveData():
    check = 'Y'
    while check == 'Y':
        user_pull = input('What stock would you like to analyze?')
        stock_info.get_live_price(user_pull)
        df = {}
        df[user_pull] = stock_info.get_data(user_pull, start_date='01/01/2019', end_date = '08/15/2021')
        #print(df[user_pull].head())
        # qf = cf.QuantFig(df[user_pull])
        # qf.add_bollinger_bands()
        # qf.add_macd()
        # qf.iplot()


        # mod = df.reset_index()
        # plt.plot(mod['Date'],df['high'])

        print(df)