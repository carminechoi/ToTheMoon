import time

import pandas as pd 
import pandas_datareader.data as pdr 
import datetime as dt

import plotly.offline as py
import plotly.graph_objs as go

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dcc.Store(id="store"),
        html.H1("Dynamically rendered tab content"),
        html.Hr(),
        dbc.Button(
            "Regenerate graphs",
            color="primary",
            block=True,
            id="button",
            className="mb-3",
        ),
        dbc.Tabs(
            [
                dbc.Tab(label="Scatter", tab_id="scatter"),
                dbc.Tab(label="Histograms", tab_id="histogram"),
            ],
            id="tabs",
            active_tab="scatter",
        ),
        html.Div(id="tab-content", className="p-4"),
    ]
)

@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)
def render_tab_content(active_tab, data):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab and data is not None:
        if active_tab == "scatter":
            return dcc.Graph(figure=data["scatter"])
        elif active_tab == "histogram":
            return dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=data["hist_1"]), width=6),
                    dbc.Col(dcc.Graph(figure=data["hist_2"]), width=6),
                ]
            )
    return "No tab selected"


@app.callback(Output("store", "data"), [Input("button", "n_clicks")])
def generate_graphs(n):
    """
    This callback generates three simple graphs from random data.
    """
    if not n:
        # generate empty graphs when app loads
        return {k: go.Figure(data=[]) for k in ["scatter", "hist_1", "hist_2"]}

    # simulate expensive graph generation process
    time.sleep(2)

    # generate 100 multivariate normal samples
    data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)

    scatter = go.Figure(
        data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
    )
    hist_1 = go.Figure(data=[go.Histogram(x=data[:, 0])])
    hist_2 = go.Figure(data=[go.Histogram(x=data[:, 1])])

    # save figures in a dictionary for sending to the dcc.Store
    return {"scatter": scatter, "hist_1": hist_1, "hist_2": hist_2}


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
    

# def plot_crypto_price(start_date, end_date, coins):
#     start = dt.datetime(start_date[0],start_date[1],start_date[2])
#     end = dt.datetime(end_date[0], end_date[1], end_date[2])
    
#     # obtain cypto price data from Yahoo
#     df = pdr.DataReader(coins, 'yahoo', start, end)

#     # allow code to display plot within notebook
#     py.init_notebook_mode(connected=True)

#     # compile all yahoo data into a variable
#     data = [go.Candlestick(x=df.index,
#                         open=df.Open,
#                         high=df.High,
#                         low=df.Low,
#                         close=df.Close)]

#     # layout information
#     layout = go.Layout(title='Bitcoin Candlestick',
#                        xaxis={'rangeslider':{'visible':False}})

#     # create figure from data and layout
#     fig = go.Figure(data=data,layout=layout)
    
#     # plot the figure into a chart
#     py.plot(fig,filename='bitcoin_candlestick.html')

# plot_crypto_price([2020,2,19], [2021,2,18], 'BTC-USD')
