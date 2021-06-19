import streamlit as st
import yfinance as yf
import pandas as pd

st.write('''
# Stock Price
These are the stock prices of the **Tesla** 

''')

symbol='TSLA'

tickerdata= yf.Ticker(symbol)

tickerdf= tickerdata.history(period='1d', start='2020-05-08', end='2021-05-08')

st.write('## About')
st.write(tickerdata.info)
st.write('## Opening Shares')
st.line_chart(tickerdf.Open)
st.write('## closing Shares')
st.line_chart(tickerdf.Close)
st.write('## Total Volume')
st.line_chart(tickerdf.Volume)
st.write('## Recommendations')
st.write(tickerdata.recommendations)
