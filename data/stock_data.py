import os
import yfinance as yf
import pandas as pd
from datetime import datetime

def get_yahoo_finance_data(ticker, start_date, end_date):
    """
    Fetches stock data from Yahoo Finance.

    Args:
        ticker (str): The stock ticker symbol.
        start_date (datetime): The start date for fetching data.
        end_date (datetime): The end date for fetching data.

    Returns:
        pd.DataFrame: Stock data fetched from Yahoo Finance.
    """
    data = yf.download(tickers=ticker, start=start_date, end=end_date)
    return data

# Create dataset folder inside the data directory
dataset_folder = os.path.join("Stock-Price-Prediction", "data", "dataset")
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

def get_data_train_test():
    """
    Main function to fetch and store stock data from Yahoo Finance.
    """
    tech_list = ['AAPL']
    for stock in tech_list:
        # Fetch data for training set (from 2019 to January 2024)
        train_start_date = datetime(2019, 1, 1)
        train_end_date = datetime(2024, 1, 31)
        train_data = get_yahoo_finance_data(stock, start_date=train_start_date, end_date=train_end_date)
        train_data.to_csv(os.path.join(dataset_folder, f"{stock}_train.csv"))

        # Fetch data for test set (from February 2024 to April 15, 2024)
        test_start_date = datetime(2024, 2, 1)
        test_end_date = datetime(2024, 4, 15)
        test_data = get_yahoo_finance_data(stock, start_date=test_start_date, end_date=test_end_date)
        test_data.to_csv(os.path.join(dataset_folder, f"{stock}_test.csv"))

def get_apple_data(start_date, end_date):
    """
    Fetches Apple stock data from Yahoo Finance.

    Args:
        start_date (datetime): The start date for fetching data.
        end_date (datetime): The end date for fetching data.

    Returns:
        pd.DataFrame: Apple stock data fetched from Yahoo Finance.
    """
    apple_data = get_yahoo_finance_data("AAPL", start_date, end_date)
    apple_data.to_csv(os.path.join(dataset_folder, "APPL.csv"))
    return apple_data

def get_data_for_info_sentiment(start_date, end_date):
    apple_data = get_yahoo_finance_data("AAPL", start_date, end_date)
    apple_data.to_csv(os.path.join(dataset_folder, "APPL_stocks.csv"))
    return apple_data
    
if __name__ == "__main__":
    # get_data_train_test()
    # get_apple_data(start_date=datetime(2019, 1, 1), end_date=datetime(2024, 4, 15))
    get_data_for_info_sentiment(start_date=datetime(2024, 3, 28), end_date=datetime(2024, 5, 1))