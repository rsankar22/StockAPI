import quandl as q
import yahooFinanceScraper as yh
import realTimeData as rtd
from forecasting import auto_regulation


#QC terms
#yhat WORKS!!! FUCK YEAH MACHINE FUCKING LEARNING
#print(type(rtd.pullLiveData()))

print(rtd.get_ticker_data_quandl('XOM'))



