import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download data
tickers = ['KO', 'PEP']
data = yf.download(tickers, start='2020-01-01', end='2024-01-01')

# Use 'Close' prices
close_prices = data['Close'][['KO', 'PEP']].copy()
close_prices.dropna(inplace=True)

# Calculate spread and Z-score
close_prices['Spread'] = close_prices['KO'] - close_prices['PEP']
mean = close_prices['Spread'].mean()
std = close_prices['Spread'].std()
close_prices['Z-Score'] = (close_prices['Spread'] - mean) / std

# Trading signals
entry_threshold = 1.0
exit_threshold = 0.0
close_prices['Long_KO_Short_PEP'] = (close_prices['Z-Score'] < -entry_threshold).astype(int)
close_prices['Short_KO_Long_PEP'] = (close_prices['Z-Score'] > entry_threshold).astype(int)
close_prices['Exit'] = (abs(close_prices['Z-Score']) < exit_threshold).astype(int)

# Plot Z-score
plt.figure(figsize=(14, 6))
plt.plot(close_prices.index, close_prices['Z-Score'], label='Z-Score', color='blue')
plt.axhline(entry_threshold, color='red', linestyle='--', label='Entry Threshold (+1)')
plt.axhline(-entry_threshold, color='green', linestyle='--', label='Entry Threshold (-1)')
plt.axhline(exit_threshold, color='black', linestyle='-.', label='Exit Threshold')
plt.axhline(-exit_threshold, color='black', linestyle='-.')
plt.title("Z-Score of KO - PEP Spread")
plt.xlabel("Date")
plt.ylabel("Z-Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("zscore_plot.png")
plt.show()
