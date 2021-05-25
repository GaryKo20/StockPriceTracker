import yfinance as yf
import streamlit as st
from PIL import Image


stonks_image = st.sidebar.image('money.png')
ticker_from_user = st.sidebar.text_input("Enter the stock ticker: ")
start_date_from_user = st.sidebar.date_input("Choose start date: ")
stop_date_from_user = st.sidebar.date_input("Choose stop date: ")


# define the ticker symbol
st.write('Shown are the stock closing price and volume of', ticker_from_user, '!')
tickerSymbol = ticker_from_user

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(
    period='1d', start=start_date_from_user, end=stop_date_from_user)

st.line_chart(tickerDf.Close)
print("\n")

# get earnings data and display on side bar
earnings_from_yfinance = tickerData.earnings
earnings_by_ticker = st.sidebar.write(ticker_from_user, "earnings data from Yahoo: ")
recommendations_side_bar = st.sidebar.write(earnings_from_yfinance)
