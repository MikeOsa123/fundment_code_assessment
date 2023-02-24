import pandas as pd
import numpy as np
import pytest

from investment_account_returns import calculate_total_time_weighted_return

@pytest.fixture
def sample_data():
    # Set up some sample data for testing
    return pd.DataFrame({
        'valuation_date': ['2017-11-15', '2017-11-16', '2017-11-17'],
        'total_valuation': [5000, 5001.47, 4990.38],
        'cash_flow': [5000, 0, 0]
    })

def test_calculate_total_time_weighted_return(sample_data):
    # Test the basic functionality of the function
    result = calculate_total_time_weighted_return(sample_data)
    expected = pd.Series([np.nan, 0.00029400000000005095, -0.0022173480996587292], name='time_weighted_return')
    pd.testing.assert_series_equal(result, expected, check_names=False)

def test_no_cash_flows():
    # Test the function with no cash flows
    data = pd.DataFrame({
        'valuation_date': ['2017-11-15', '2017-11-16', '2017-11-17'],
        'total_valuation': [5000, 5500, 6000],
        'cash_flow': [0, 0, 0]
    })
    result = calculate_total_time_weighted_return(data)
    expected = pd.Series([np.nan, 0.1, 0.090909], name='time_weighted_return')
    pd.testing.assert_series_equal(result, expected)

def test_single_day():
    # Test the function with only one day of data
    data = pd.DataFrame({
        'valuation_date': ['2017-11-15'],
        'total_valuation': [5000],
        'cash_flow': [5000]
    })
    result = calculate_total_time_weighted_return(data)
    expected = pd.Series([np.nan], name='time_weighted_return')
    pd.testing.assert_series_equal(result, expected)

def test_missing_data():
    # Test the function with missing data
    with pytest.raises(Exception):
        data = pd.DataFrame({
        'valuation_date': ['2017-11-15', '2017-11-17'],
        'total_valuation': [5000, 4990.38],
        'cash_flow': [5000]
        })
        calculate_total_time_weighted_return(data)
