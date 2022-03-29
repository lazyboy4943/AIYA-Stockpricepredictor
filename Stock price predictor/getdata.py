# gets data from yahoo finance

# imports
import pandas as pd
import yfinance as yf
import yahoofinancials as YahooFinancials


aapl_df = yf.download('AAPL', 
                      start='2019-01-01', 
                      end='2021-06-12', 
                      progress=False,
)
aapl_df.head()
