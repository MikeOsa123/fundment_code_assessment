import pandas as pd

def calculate_total_time_weighted_return(data: pd.DataFrame) -> pd.Series:
    # First, we'll create a new column for the daily returns
    data['time_weighted_return'] = data['total_valuation'].diff() / (data['total_valuation'].shift(1) + data['cash_flow'])
    
    # We'll return a pd.Series with the TWR for each period
    return data['time_weighted_return']
