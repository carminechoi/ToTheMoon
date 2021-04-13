#%%
import pandas as pd 
import pandas_datareader.data as pdr 
import datetime as dt

import plotly.offline as py
import plotly.graph_objs as go


def plot_crypto_price(start_date, end_date, coins):
    start = dt.datetime(start_date[0],start_date[1],start_date[2])
    end = dt.datetime(end_date[0], end_date[1], end_date[2])
    
    # obtain cypto price data from Yahoo
    df = pdr.DataReader(coins, 'yahoo', start, end)

    # allow code to display plot within notebook
    py.init_notebook_mode(connected=True)

    # compile all yahoo data into a variable
    data = [go.Candlestick(x=df.index,
                        open=df.Open,
                        high=df.High,
                        low=df.Low,
                        close=df.Close)]

    # layout information
    layout = go.Layout(title='Bitcoin Candlestick',
                       xaxis={'rangeslider':{'visible':False}})

    # create figure from data and layout
    fig = go.Figure(data=data,layout=layout)
    
    # plot the figure into a chart
    py.plot(fig,filename='bitcoin_candlestick.html')

plot_crypto_price([2020,2,19], [2021,2,18], 'BTC-USD')
# %%
