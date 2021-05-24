import yfinance as yf
import streamlit as st

# st.write('Shown are the stock closing price and volume of',ticker_from_user,'!')

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
ticker_from_user = st.text_input("Enter the stock ticker: ")
st.write('Shown are the stock closing price and volume of',ticker_from_user,'!')
tickerSymbol = ticker_from_user
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-24')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)

