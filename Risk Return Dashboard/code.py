import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# getting the tickers
tickers = ["BRK-B", "JPM", "LYG", "MCD", "V", "NVDA", "VOO"]

# closing data from the year 2025
data = yf.download(tickers, start="2024-09-30", end="2025-09-30")["Close"]

# daily returns
returns = data.pct_change().dropna()

trading_days = 252

# annualized mean return (compound growth approx)
annual_return = (1 + returns.mean())**trading_days - 1  

# annualized volatility
annual_volatility = returns.std() * (trading_days**0.5)

# annualized Sharpe ratio
rf_annual = 0.0415
risk_return = pd.DataFrame({
    "Mean Return": annual_return,
    "Volatility": annual_volatility
})
risk_return["Sharpe Ratio"] = (risk_return["Mean Return"] - rf_annual) / risk_return["Volatility"]

print(risk_return)

# graph
plt.figure(figsize=(8,6))
sc = plt.scatter(
    risk_return["Volatility"]*100, 
    risk_return["Mean Return"]*100, 
    c=risk_return["Sharpe Ratio"], 
    cmap="coolwarm", 
    s=120, edgecolor="k"
)

# add labels
for ticker in risk_return.index:
    plt.annotate(ticker, 
                 (risk_return.loc[ticker, "Volatility"]*100, 
                  risk_return.loc[ticker, "Mean Return"]*100),
                 textcoords="offset points", xytext=(5,5))

plt.title("Risk-Return Plot with Sharpe Ratios (2025)")
plt.xlabel("Annualized Volatility (%)")
plt.ylabel("Annualized Mean Return (%)")
plt.colorbar(sc, label="Sharpe Ratio")
plt.grid(True)
plt.savefig(r"C:\Users\Gladys\Documents\GitHub\quantFinance\Quant-Finance\Risk Return Dashboard\sharpe_ratios.png", 
            dpi=300, bbox_inches="tight")
plt.show()
