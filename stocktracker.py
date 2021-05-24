import yfinance as yf
import streamlit as st


#define the ticker symbol
ticker_from_user = st.text_input("Enter the stock ticker: ")
start_date_from_user = st.date_input("choose start date: ")
stop_date_from_user = st.date_input("choose stop date:")
st.write('Shown are the stock closing price and volume of',ticker_from_user,'!')
tickerSymbol = ticker_from_user
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start=start_date_from_user, end=stop_date_from_user)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)

