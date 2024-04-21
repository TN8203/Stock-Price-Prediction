import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.graphics.tsaplots as tsaplots

# Historical view of the closing prices for one company
def plot_historical_closing_prices(company, title):
    """
    Plot historical view of the closing prices for a single company.

    Args:
        company (DataFrame): DataFrame containing historical stock data of a single company.
        title (str): Title for the plot.
    """
    plt.figure(figsize=(20, 5))
    plt.plot(company["Date"], company["Adj Close"])
    plt.title(title)
    plt.ylabel('Adj Close')
    plt.tight_layout()
    plt.show()

# Total volume of stock being traded each day for one company
def plot_total_volume_traded(company, title):
    """
    Plot the total volume of stock traded each day for a single company.

    Args:
        company (DataFrame): DataFrame containing historical stock data of a single company.
        title (str): Title for the plot.
    """
    plt.figure(figsize=(20, 5))
    plt.plot(company["Date"], company["Volume"])
    plt.title(title)
    plt.ylabel('Volume')
    plt.tight_layout()
    plt.show()

# Moving averages of the various stocks for one company
def plot_moving_averages(company, title, moving_averages=[10, 20, 50]):
    """
    Plot moving averages for a single company.

    Args:
        company (DataFrame): DataFrame containing historical stock data of a single company.
        title (str): Title for the plot.
        moving_averages (list): List of moving average periods to calculate.
    """
    for moving_average in moving_averages:
        column_name = f'Moving Average for {moving_average} days'
        company[column_name] = company["Adj Close"].rolling(moving_average).mean()

    plt.figure(figsize=(20, 5))
    plt.plot(company["Date"], company["Adj Close"])
    for moving_average in moving_averages:
        plt.plot(company["Date"], company[f"Moving Average for {moving_average} days"])
    plt.title(title)
    plt.legend(["Adj Close"] + [f"Moving Average for {moving_average} days" for moving_average in moving_averages])
    plt.tight_layout()
    plt.show()

# Daily Return on average
def plot_daily_returns(company, title):
    """
    Plot daily returns for a single company.

    Args:
        company (DataFrame): DataFrame containing historical stock data of a single company.
        title (str): Title for the plot.
    """
    plt.figure(figsize=(20, 5))
    plt.plot(company["Date"], company["Daily Return"])
    plt.title(title)
    plt.ylabel('Daily Return')
    plt.tight_layout()
    plt.show()

def plot_daily_returns_distribution(company, title):
    """
    Plot the distribution of daily returns for a single company.

    Args:
        company (DataFrame): DataFrame containing historical stock data for a single company.
        title (str): Title for the plot.
    """
    plt.figure(figsize=(20, 5))
    sns.distplot(company["Daily Return"].dropna(), color="purple")
    plt.title(title)
    plt.xlabel('Daily Return')
    plt.show()

def print_kurtosis_value(company, title):
    """
    Print the kurtosis value for the daily returns of a single company.

    Args:
        company (DataFrame): DataFrame containing historical stock data for a single company.
        title (str): Title for the company.
    """
    print(f'Kurtosis Value for {title}: {company["Daily Return"].kurtosis()}')

# Risk analysis
def plot_risk_return(returns_df, companies_title):
    """
    Plot risk-return relationship for multiple companies.

    Args:
        returns_df (DataFrame): DataFrame containing percentage daily returns of multiple companies.
        companies_title (list): List of titles for each company.
    """
    returns = returns_df.drop("Date", axis=1).dropna()

    area = np.pi * 20
    plt.scatter(returns.mean(), returns.std(), s=area)
    
    # Set the x and y limits of the plot
    plt.xlim([-0.0025, 0.0025])
    plt.ylim([0.001, 0.025])

    # Set the plot axis titles
    plt.xlabel('Expected returns')
    plt.ylabel('Risk')

    # Label the scatter plots without arrows
    for label, x, y in zip(companies_title, returns.mean(), returns.std()):
        plt.annotate(f'{label}: ({x:.4f}, {y:.4f})', xy=(x, y), xytext=(0, 10), textcoords='offset points')
        
    plt.title('Risk-Return Relationship')
    plt.show()

# Dickey-Fuller Method to check stationary and seasonality
def tsplot(y, lags=None, figsize=(14, 8), style='bmh'):
    """
    Plot time series data along with autocorrelation and partial autocorrelation functions,
    and perform the Dickey-Fuller test for stationarity.
    
    Parameters:
    - y: Time series data (can be a list, array, or Pandas Series).
    - lags: Number of lags to include in the ACF and PACF plots.
    - figsize: Tuple specifying the size of the plot.
    - style: Plotting style to use (default is 'bmh').
    """
    # Convert input data to Pandas Series if not already
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
        
    # Set the plotting style
    with plt.style.context(style=style):
        fig = plt.figure(figsize=figsize)
        layout=(2,2)
        
        # Create subplots
        ts_ax = plt.subplot2grid(layout, (0,0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1,0))
        pacf_ax = plt.subplot2grid(layout, (1,1))
        
        # Plot time series data
        y.plot(ax=ts_ax)
        
        # Compute p-value using Dickey-Fuller test
        p_value = sm.tsa.stattools.adfuller(y)[1]
        ts_ax.set_title('Time Series Analysis Plots\n Dickey-Fuller: p={0:.5f}'.format(p_value))
        
        # Plot autocorrelation function (ACF)
        tsaplots.plot_acf(y, lags=lags, ax=acf_ax)
        
        # Plot partial autocorrelation function (PACF)
        tsaplots.plot_pacf(y, lags=lags, ax=pacf_ax)
        
        # Adjust subplot layout
        plt.tight_layout()