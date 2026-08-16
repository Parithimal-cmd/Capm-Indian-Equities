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
return volatility. Daily volatility was then calculated using 252 trading
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
### Key Findings
- M&M had the highest estimated beta (1.192), indicating the greatest
  sensitivity to NIFTY 50 market movements among the selected stocks.
- Sun Pharma had the lowest beta (0.576), indicating relatively lower
  market sensitivity.
- M&M also had the highest annualized volatility (28.71%), while ITC had
  the lowest (20.32%).
- Four of the eight stocks had beta values above 1: HDFC Bank, Larsen &
  Toubro, M&M, and Reliance.
- Beta was statistically significant for all eight stocks.
  ## CAPM Validation
To examine the CAPM prediction that higher systematic risk should be
associated with higher average returns, a cross-sectional analysis was
conducted using the estimated beta and average daily return of the eight
selected stocks.
The beta-return correlation was approximately **0.115**, indicating a very
weak positive relationship between beta and average return.
A cross-sectional OLS regression was then estimated using average daily
return as the dependent variable and beta as the explanatory variable.
The regression produced:
- **Beta coefficient:** 0.000219
- **Beta p-value:** 0.787
- **R²:** 0.0131
The beta coefficient was not statistically significant, and the low R²
indicates that beta explained very little of the variation in average
returns across the selected stocks.
Therefore, the sample provides **limited empirical support for the
CAPM-predicted positive beta-return relationship**.
## Visualizations
The project includes four visualizations:
1. **CAPM Beta Comparison** – compares the estimated beta of the selected
   stocks and their sensitivity to NIFTY 50 market movements.
2. **Annualized Stock Volatility** – compares the annualized volatility of
   the selected stocks based on their daily returns.
3. **Residuals vs Fitted Values** – provides a regression diagnostic for the
   Reliance CAPM model.
4. **Beta vs Average Return** – visualizes the cross-sectional relationship
   between estimated beta and average daily return.
   ## Limitations
- The analysis is based on a relatively small sample of eight selected
  Indian equities rather than the entire NSE.
- The cross-sectional CAPM test is based on only eight observations, which
  limits the statistical power of the analysis.
- Historical average returns are used as a proxy for expected returns,
  although CAPM is fundamentally a model of expected returns.
- The analysis uses the NIFTY 50 as the market benchmark, which may not
  capture all sources of systematic risk in the Indian equity market.
  ## Conclusion
This project examined the CAPM relationship using eight selected NSE-listed
Indian equities and the NIFTY 50 as the market benchmark. The CAPM
regressions showed that the stocks differed substantially in their
sensitivity to market movements, with estimated beta values ranging from
0.576 for Sun Pharma to 1.192 for M&M.
The cross-sectional analysis, however, found only a weak positive
relationship between beta and average return, with a correlation of
approximately 0.115. The beta coefficient was not statistically significant
(p = 0.787), and the regression had a low R² of 0.0131.
Therefore, the selected sample provides limited empirical support for the
positive beta-return relationship predicted by CAPM. The results should be
interpreted in the context of the small sample size and the limitations of
using historical average returns to represent expected returns.
