import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === Step 1: Download data ===
tickers = ['KO', 'PEP']
data = yf.download(tickers, start='2020-01-01', end='2024-01-01')['Close']

# === Step 2: Calculate Spread and Z-Score ===
data['spread'] = data['KO'] - data['PEP']
data['zscore'] = (data['spread'] - data['spread'].mean()) / data['spread'].std()

# === Step 3: Generate Trading Signals ===
data['position_KO'] = 0
data['position_PEP'] = 0

# Long KO, Short PEP when zscore < -1
data.loc[data['zscore'] < -1, ['position_KO', 'position_PEP']] = [1, -1]

# Short KO, Long PEP when zscore > 1
data.loc[data['zscore'] > 1, ['position_KO', 'position_PEP']] = [-1, 1]

# Exit both when zscore between -0.5 and 0.5
data.loc[(data['zscore'] > -0.5) & (data['zscore'] < 0.5), ['position_KO', 'position_PEP']] = [0, 0]

# Forward-fill the positions
data[['position_KO', 'position_PEP']] = data[['position_KO', 'position_PEP']].ffill()

# === Step 4: Calculate Strategy Returns ===
data['returns_KO'] = data['KO'].pct_change()
data['returns_PEP'] = data['PEP'].pct_change()

# Daily strategy return
data['strategy_returns'] = data['position_KO'] * data['returns_KO'] + data['position_PEP'] * data['returns_PEP']
data['cumulative_returns'] = (1 + data['strategy_returns'].fillna(0)).cumprod()

# === Step 5: Plot Cumulative Returns ===
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['cumulative_returns'], label='Pair Trading Strategy', color='blue')
plt.plot(data.index, (1 + data['returns_KO'].fillna(0)).cumprod(), label='KO Buy & Hold', linestyle='--', color='orange')
plt.plot(data.index, (1 + data['returns_PEP'].fillna(0)).cumprod(), label='PEP Buy & Hold', linestyle='--', color='green')
plt.title('Cumulative Returns: Pair Trading vs Buy & Hold')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("Cumulative_Returns.png")
plt.show()
