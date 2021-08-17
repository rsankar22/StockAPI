import quandl as q
import matplotlib.pyplot as plt
import pandas as pd
import realTimeData as rtd


q.ApiConfig.api_key = 'uRicrbBWVB_gVXxbS72V'
mydata = q.get_table('SHARADAR/SEP')
#QC terms


rtd.pullLiveVisual()

#search for ticker
# def search(arr, target):
#     target_arr = arr[arr['ticker'] == target]
#     return target_arr
#
#
# check = 'Y'
# while check == 'Y':
#     user = input('Choose ticker: ')
#     subarray = search(mydata,user)
#     print(subarray)
#     plt.plot(subarray['date'],subarray['high'])
#     title = 'Ticker: ', user
#     plt.title(title)
#     plt.xlabel('Date')
#     plt.ylabel('Price ($ USD)')
#     check = input('Continue Analyses [Y/N]?')
#     plt.show()



