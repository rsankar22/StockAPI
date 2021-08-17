import quandl as q
import yahooFinanceScraper as yh
import pandas as pd
import realTimeData as rtd


q.ApiConfig.api_key = 'uRicrbBWVB_gVXxbS72V'
mydata = q.get_table('SHARADAR/SEP')
#QC terms


#rtd.pullLiveVisual()
print(yh.getHeaderData())




