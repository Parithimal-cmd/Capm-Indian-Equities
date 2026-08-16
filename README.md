# Capm-Indian-Equities
Capm validation and analysis of Indian equity markets
## Objective
The objective of this project is to empirically examine the validity of the CAPM in selected Indian equities. First, we analyzed eight selected Indian
stocks against the NIFTY 50 index to estimate their market sensitivity,systematic risk, and return volatility. We then conducted a cross-sectional
analysis to empirically examine whether stocks with higher systematic risk (beta) provided higher average returns, as predicted by CAPM.
## Data
The analysis uses daily stock-market data for eight selected NSE-listed
Indian equities, with the NIFTY 50 index used as the market benchmark.
### Selected Stocks
- Reliance Industries
- TCS
- HDFC Bank
- ITC
- Larsen & Toubro
- Sun Pharmaceutical Industries
- Bharti Airtel
- Mahindra & Mahindra
### Data Details
- **Market:** Indian equity market
- **Benchmark:** NIFTY 50
- **Period:** January 2021 – August 2026
- **Frequency:** Daily
- **Price variable:** Closing price
- **Return measure:** Daily percentage return
- **Data source:** Yahoo Finance
- **Python library:** `yfinance
## Methodology
The analysis was conducted in several stages.
### 1. Return Calculation
Daily returns for each stock and the NIFTY 50 were calculated from their
daily closing prices using percentage changes.
### 2. CAPM Regression
For each of the eight selected stocks, an Ordinary Least Squares (OLS)
regression was conducted using the NIFTY 50 return as the market return.
The CAPM regression was specified as:
R_i = α_i + β_i R_m + ε_i
where:
- **R_i** = return of the individual stock
- **R_m** = NIFTY 50 market return
- **α_i** = alpha (intercept)
- **β_i** = beta, measuring the stock's sensitivity to market movements
- **ε_i** = regression residual
The regression results were used to estimate alpha, beta, R-squared, and the
statistical significance of beta.
### 3. Volatility Analysis
The standard deviation of daily stock returns was calculated to measure
return volatility. Daily volatility was then annualized using 252 trading
days.
### 4. Cross-Sectional CAPM Analysis
After estimating the beta of each stock, a cross-sectional analysis was
conducted using the estimated beta and average daily return of each stock.
The beta-return correlation and an OLS regression were used to examine
whether stocks with higher systematic risk tended to have higher average
returns, as predicted by CAPM.
## CAPM Framework
The Capital Asset Pricing Model (CAPM) describes the relationship between
systematic risk and expected return. It proposes that investors should be
compensated for taking systematic market risk.
The theoretical CAPM relationship is:
R_i = R_f + β_i(R_m - R_f)
where:
- **R_i** = expected return of stock *i*
- **R_f** = risk-free rate
- **β_i** = beta of stock *i*, measuring its sensitivity to market movements
- **R_m** = expected return of the market
- **(R_m - R_f)** = market risk premium
A key prediction of CAPM is that stocks with higher systematic risk (higher
beta) should, on average, provide higher expected returns.
In this project, the NIFTY 50 is used as the market benchmark to estimate
the beta of the selected Indian equities. The empirical beta-return
relationship is then examined using a cross-sectional analysis.
## Results
### CAPM Regression Results
The CAPM regression was estimated separately for each of the eight selected
stocks using the NIFTY 50 as the market benchmark.
The main regression outputs were alpha, beta, R-squared, and the p-value of
beta.
The complete regression results are available in
`CAPM_Results.csv`.
