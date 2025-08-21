from alpha_vantage.timeseries import TimeSeries
import pandas as pd

API_KEY = "JBHAGL8721EUDN6N"

def get_stock_data(symbol="AAPL", outputsize="full"):
    ts = TimeSeries(key=API_KEY, output_format="pandas")
    data, meta_data = ts.get_daily(symbol=symbol, outputsize=outputsize)
    
    data = data.sort_index()
    
    data = data.rename(columns={
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })
    return data

if __name__ == "__main__":
    df = get_stock_data("AAPL")  
    print(df.head())              
    df.to_csv("AAPL.csv")         
