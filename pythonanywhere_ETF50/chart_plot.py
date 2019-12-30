import numpy as np
import pandas as pd
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

#import tushare as ts
#etf = ts.get_hist_data('510050',start='2018-01-01',end='2018-06-30')
etf = pd.read_csv('etf50.csv')
etf = etf.set_index('date')


class Chart_Plot:
    def __init__(self):
        pass
    def candle_stick(self):#日K线图
        candle_trace = go.Candlestick(x = etf.index,
                                      open = etf.open,
                                      high = etf.high,
                                      low = etf.low,
                                      close = etf.close,
                                      increasing=dict(line=dict(color= '#ff0000')),
                                      decreasing=dict(line=dict(color= '#00ff00')),
                                      name = 'ETF50')
        candle_data = [candle_trace]
        candle_layout = {'title': 'ETF50','yaxis': {'title': '价格'}}
        candle_fig = dict(data=candle_data, layout=candle_layout)
        div = pyplt(candle_fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
        return div
    
    def twoline_graph(self): #半年线图
        close = etf['close'].tolist()
        date = etf.index.tolist()
        trace = [go.Scatter(
                            x=date,
                            y=close
                            )]
        layout = dict(
              title='ETF50',
              xaxis=dict(title='日期'),
              yaxis=dict(title='价格')
              )
        fig = dict(data=trace, layout=layout)
        div = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
        return div


