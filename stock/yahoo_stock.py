import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010,1,1,)
end = datetime.datetime(2015,12,31)

df = web.DataReader("078930.KS", "yahoo", start, end)
print(df)