# 📈 Kalman Filter-Based Statistical Arbitrage Strategy

This project implements a dynamic **pair trading strategy** using a **Kalman Filter** to estimate time-varying hedge ratios between co-integrated stock pairs. Unlike traditional static linear regression, this approach adapts to changing market regimes using a **state-space model**, enhancing responsiveness and trading signal accuracy.

---

## 🧠 Strategy Overview

- **Objective:** Generate alpha by exploiting the mean-reverting relationship between two co-integrated stocks.
- **Technique:** Use a **Kalman Filter** to dynamically estimate the hedge ratio (β) and intercept, forming a spread that adapts over time.
- **Signal Generation:** Apply **Z-score normalization** on the filtered spread to generate **Buy/Sell/Exit** signals based on predefined thresholds.
- **Risk Management:** Includes **position sizing**, **stop-loss**, and **take-profit** mechanisms.

---

## 📊 Key Features

- ✅ Dynamic estimation of hedge ratio using Kalman Filter (`pykalman`)
- ✅ Time-series preprocessing with `yfinance`, `pandas`
- ✅ Z-score based signal generation
- ✅ Trade execution logic with stop-loss and take-profit
- ✅ Performance evaluation and visualization with annotated plots
- ✅ Fully backtestable strategy pipeline

---
![plot](Kalman%20Filter-based%20pair%20trading%20strategy/Plot.png)
## 🔧 Tools & Libraries

- Python 3.x  
- [`pandas`](https://pandas.pydata.org/)  
- [`yfinance`](https://pypi.org/project/yfinance/)  
- [`pykalman`](https://pypi.org/project/pykalman/)  
- [`matplotlib`](https://matplotlib.org/)


