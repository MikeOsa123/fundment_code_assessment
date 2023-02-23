import pandas as pd
import numpy as np
import pytest

from investment_account_returns import calculate_total_time_weighted_return


def test_calculate_total_time_weighted_return():
    # Create a sample DataFrame with various edge cases
    data = pd.DataFrame({
        'valuation_date': pd.date_range('2020-01-01', periods=10, freq='D'),
        'total_valuation': [1000, 2000, np.nan, 3000, 4000, 5000, 6000, 7000, 8000, 9000],
        'cash_flow': [0, 1000, 2000, -3000, -4000, 5000, np.nan, 7000, 8000, 9000]
    })
    
    # Calculate the time-weighted returns
    returns = calculate_total_time_weighted_return(data)
    
    # Assert that the result has the expected length and type
    assert len(returns) == 10
    assert isinstance(returns, pd.Series)
    
    # Assert that the time-weighted returns are calculated correctly
    assert np.allclose(returns, [
        0.0,
        0.0,
        np.nan,
        0.0,
        0.0,
        0.1667,
        np.nan,
        0.4713,
        0.5319,
        0.5886
    ], equal_nan=True)

def test_calculate_total_time_weighted_return_handles_missing_data():
    data_missing = pd.DataFrame({
        'valuation_date': pd.date_range('2020-01-01', periods=3, freq='D'),
        'total_valuation': [1000, np.nan, 2000],
        'cash_flow': [0, 1000, np.nan]
    })
    returns_missing = calculate_total_time_weighted_return(data_missing)
    assert np.all(np.isnan(returns_missing))
    

def test_calculate_total_time_weighted_return_handles_small_datasets():
    data_small = pd.DataFrame({
        'valuation_date': pd.date_range('2020-01-01', periods=2, freq='D'),
        'total_valuation': [1000, 2000],
        'cash_flow': [0, 1000]
    })
    returns_small = calculate_total_time_weighted_return(data_small)
    assert np.allclose(returns_small, [0.0, 0.6931])


def test_calculate_total_time_weighted_return_handles_negative_cashflow():
    data_negative = pd.DataFrame({
        'valuation_date': pd.date_range('2020-01-01', periods=3, freq='D'),
        'total_valuation': [1000, 2000, 3000],
        'cash_flow': [0, -1000, -2000]
    })
    returns_negative = calculate_total_time_weighted_return(data_negative)
    assert np.allclose(returns_negative, [0.0, -0.3030, -0.1756])


def test_calculate_total_time_weighted_return_handles_zero_valuations():
    data_zero = pd.DataFrame({
        'valuation_date': pd.date_range('2020-01-01', periods=3, freq='D'),
        'total_valuation': [0, 1000, 2000],
        'cash_flow': [0, 1000, 2000]
    })
    returns_zero = calculate_total_time_weighted_return(data_zero)
    assert np.allclose(returns_zero, [0.0, 0.0, 0.6931])
