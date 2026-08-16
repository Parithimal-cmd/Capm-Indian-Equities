# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 08:37:18 2026

@author: parit
"""

# -*- coding: utf-8 -*-
"""
CAPM Validation & Beta Analysis in Indian Equity Markets

Author: Parit
"""

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import yfinance as yf
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


# ============================================================
# 2. DOWNLOAD STOCK DATA
# ============================================================

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "HDFCBANK.NS",
    "ITC.NS",
    "LT.NS",
    "SUNPHARMA.NS",
    "BHARTIARTL.NS",
    "M&M.NS"
]

stock_data = yf.download(
    stocks,
    start="2021-01-01"
)


# ============================================================
# 3. CALCULATE STOCK RETURNS
# ============================================================

close_price = stock_data["Close"]

stock_returns = close_price.pct_change()
stock_returns = stock_returns.dropna()


# ============================================================
# 4. DOWNLOAD NIFTY 50 DATA
# ============================================================

nifty = yf.download(
    "^NSEI",
    start="2021-01-01"
)

nifty_close = nifty["Close"]

nifty_returns = nifty_close.pct_change()
nifty_returns = nifty_returns.dropna()


# ============================================================
# 5. COMBINE STOCK AND NIFTY RETURNS
# ============================================================

data = stock_returns.join(
    nifty_returns,
    how="inner"
)

data = data.rename(
    columns={"^NSEI": "NIFTY_Return"}
)


# ============================================================
# 6. DEFINE STOCK COLUMNS
# ============================================================

stock_columns = [
    "BHARTIARTL.NS",
    "HDFCBANK.NS",
    "ITC.NS",
    "LT.NS",
    "M&M.NS",
    "RELIANCE.NS",
    "SUNPHARMA.NS",
    "TCS.NS"
]


# ============================================================
# 7. CAPM TIME-SERIES REGRESSIONS
# ============================================================

results = {}

for stock in stock_columns:

    Y = data[stock]

    X = data["NIFTY_Return"]
    X = sm.add_constant(X)

    model = sm.OLS(Y, X)
    result = model.fit()

    results[stock] = result


# ============================================================
# 8. EXTRACT CAPM RESULTS
# ============================================================

results_table = []

for stock in stock_columns:

    result = results[stock]

    results_table.append({
        "Stock": stock,
        "Alpha": result.params["const"],
        "Beta": result.params["NIFTY_Return"],
        "R_squared": result.rsquared,
        "Beta_pvalue": result.pvalues["NIFTY_Return"]
    })

results_df = pd.DataFrame(results_table)


# ============================================================
# 9. CALCULATE ANNUALIZED VOLATILITY
# ============================================================

volatility = stock_returns.std()

annual_volatility = volatility * (252 ** 0.5)

results_df["Annual_Volatility"] = (
    results_df["Stock"].map(annual_volatility)
)


# ============================================================
# 10. BETA CHART
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    results_df["Stock"],
    results_df["Beta"]
)

plt.xlabel("Stock")
plt.ylabel("Beta")
plt.title("CAPM Beta of Selected Stocks")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 11. ANNUALIZED VOLATILITY CHART
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    results_df["Stock"],
    results_df["Annual_Volatility"]
)

plt.xlabel("Stock")
plt.ylabel("Annualized Volatility")
plt.title("Annualized Stock Volatility")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 12. RESIDUAL DIAGNOSTIC - RELIANCE
# ============================================================

result = results["RELIANCE.NS"]

fitted = result.fittedvalues
residuals = result.resid

plt.figure(figsize=(10, 6))

plt.scatter(
    fitted,
    residuals
)

plt.axhline(y=0)

plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted Values - Reliance")

plt.tight_layout()
plt.show()


# ============================================================
# 13. CAPM CROSS-SECTIONAL VALIDATION
# ============================================================

average_returns = stock_returns.mean()

results_df["Average_Return"] = (
    results_df["Stock"].map(average_returns)
)


# Beta vs Average Return

plt.figure(figsize=(10, 6))

plt.scatter(
    results_df["Beta"],
    results_df["Average_Return"]
)

plt.xlabel("CAPM Beta")
plt.ylabel("Average Daily Return")
plt.title("Beta vs Average Daily Return")

plt.tight_layout()
plt.show()


# Correlation between Beta and Average Return

correlation = results_df["Beta"].corr(
    results_df["Average_Return"]
)

print("Beta-Return Correlation:", correlation)


# Cross-sectional regression

X = results_df["Beta"]
X = sm.add_constant(X)

Y = results_df["Average_Return"]

capm_test = sm.OLS(Y, X).fit()

print(capm_test.summary())


# ============================================================
# 14. DISPLAY AND SAVE FINAL RESULTS
# ============================================================

print("\nFinal Results:")
print(results_df)
results_df.to_csv("CAPM_analysis.csv", index=False)

