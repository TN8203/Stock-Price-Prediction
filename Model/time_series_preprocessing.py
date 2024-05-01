import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

def test_stationarity(timeseries):
    """
    Test stationarity of a time series.

    Args:
    - timeseries (pd.Series): The time series to test.

    Returns:
    - None
    """
    # Calculate rolling statistics
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()

    # Plot rolling statistics
    plt.plot(timeseries, color='blue', label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show()

    # Perform Dickey-Fuller test
    print("Results of Dickey-Fuller Test:")
    adft = adfuller(timeseries, autolag='AIC')
    output = pd.Series(adft[0:4], index=['Test Statistics', 'p-value', 'No. of Lags Used', 'Number of Observations Used'])
    for key, value in adft[4].items():
        output['Critical Value (%s)' % key] = value
    print(output)

def decompose_seasonality(timeseries):
    """
    Decompose the seasonality of a time series.

    Args:
    - timeseries (pd.Series): The time series to decompose.

    Returns:
    - None
    """
    result = seasonal_decompose(timeseries, model='multiplicative', period=12)
    fig = plt.figure()
    fig = result.plot()
    fig.set_size_inches(16, 9)
    plt.show()

def eliminate_trend(timeseries):
    """
    Eliminate trend from a time series.

    Args:
    - timeseries (pd.Series): The time series to eliminate trend.

    Returns:
    - tuple: A tuple containing the detrended time series, the moving average, and the standard deviation.
    """
    df_log = np.log(timeseries)
    moving_avg = df_log.rolling(12).mean()
    std_dev = df_log.rolling(12).std()
    detrended_series = df_log - moving_avg
    return df_log, detrended_series, moving_avg, std_dev
