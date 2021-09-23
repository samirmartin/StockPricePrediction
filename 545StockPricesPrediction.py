import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import sys
import warnings
import kats as k
from kats.consts import TimeSeriesData


stock_df = pd.read_table("/Users/samirmartin/Desktop/Data_Engineering-545/StockPricesGroupProject/fivesecbars.csv", delimiter=",")
stock_0 = stock_df.loc[stock_df["tickerid"] == 0]
stock_0 = stock_0[['epochtime','close']]
stock_0.columns = ["time", "value"]
plt.plot(stock_0['value'])
plt.show()

stock_1 = stock_df.loc[stock_df["tickerid"] == 1]
stock_2 = stock_df.loc[stock_df["tickerid"] == 2]
stock_3 = stock_df.loc[stock_df["tickerid"] == 3]
stock_4 = stock_df.loc[stock_df["tickerid"] == 4]




stock_df.columns = ["time", "value"]
stock_df.head()
stock_ts = TimeSeriesData(stock_df)

# check that the type of the data is a "TimeSeriesData" object for both cases
print(type(stock_ts))
# For the air_passengers TimeSeriesData, check that both time and value are pd.Series
print(type(stock_ts.time))
print(type(stock.value))

stock_ts_from_series = TimeSeriesData(time=stock_df.time, value=stock_df.value)
use_unix_time = True
unix_time_units="s"

ts_from_unixtime = TimeSeriesData(
        time=stock_ts_unixtime, 
        value=stock_df.value, 
        use_unix_time=True, 
        unix_time_units="s"
)
ts_from_unixtime


%matplotlib inline

# Must pass the name of the value columns to plot
stock_ts.plot(cols=['value'])
plt.show()






# import the param and model classes for Prophet model
from kats.models.prophet import ProphetModel, ProphetParams

# create a model param instance
params = ProphetParams(seasonality_mode='multiplicative') # additive mode gives worse results

# create a prophet model instance
m = ProphetModel(stocks_ts, params)

# fit model simply by calling m.fit()
m.fit()

# make prediction for next 30 month
fcst = m.predict(steps=30, freq="MS")

# the predict method returns a dataframe as follows
fcst.head()

# visualize the results with uncertainty intervals
m.plot()