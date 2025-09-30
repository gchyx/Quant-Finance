import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# getting the tickers
tickers = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOG", "NVDA"]

# closing data from the year 2024
data = yf.download(tickers, start="2024-01-01", end="2025-01-01")["Close"]

# getting the returns and the volatility
returns = data.pct_change().dropna()

risk_return = pd.DataFrame({
    "Mean Return": returns.mean(),
    "Volatility": returns.std()
})
print(risk_return)

# graph
plt.figure(figsize=(8,6))
plt.scatter(risk_return["Volatility"], risk_return["Mean Return"], s=100)

# add labels for each ticker
for ticker in risk_return.index:
    plt.annotate(ticker, 
                 (risk_return.loc[ticker, "Volatility"], 
                  risk_return.loc[ticker, "Mean Return"]),
                 textcoords="offset points", xytext=(5,5))

plt.title("Risk-Return Plot (Daily Returns)")
plt.xlabel("Volatility (Risk)")
plt.ylabel("Mean Daily Return")
plt.grid(True)
plt.show()