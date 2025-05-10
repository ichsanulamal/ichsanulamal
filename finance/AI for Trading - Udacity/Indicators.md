### **Moving Average (MA)**
The Moving Average is the average of a security's price over a specified number of periods. The formula is:

\[
\text{MA}_n = \frac{P_1 + P_2 + \dots + P_n}{n}
\]

- \(P_1, P_2, \dots, P_n\) are the prices at each period.
- \(n\) is the number of periods.

### **Exponential Moving Average (EMA)**
The Exponential Moving Average gives more weight to recent prices. The formula is:

\[
\text{EMA}_t = \left({P_t \times \alpha} + \text{EMA}_{t-1} \times (1 - \alpha)\right)
\]

Where:

\[
\alpha = \frac{2}{n + 1}
\]

- \(P_t\) is the current price.
- \(\text{EMA}_{t-1}\) is the EMA value of the previous period.
- \(n\) is the number of periods.

### **Bollinger Bands (BOLL)**
Bollinger Bands consist of a middle band (which is usually a 20-period MA) and two outer bands. The formula is:

- **Middle Band (MB):** \( \text{MB} = \text{MA}_n \)
  
- **Upper Band (UB):** \( \text{UB} = \text{MB} + (k \times \sigma) \)

- **Lower Band (LB):** \( \text{LB} = \text{MB} - (k \times \sigma) \)

Where:

- \( \sigma \) is the standard deviation of the prices over the past \(n\) periods.
- \( k \) is the number of standard deviations away from the middle band, typically set to 2.

### **Parabolic SAR (SAR)**
The **Parabolic SAR** (Stop and Reverse) is calculated using the following formula:

- **SAR Current = SAR Previous + [AF * (EP - SAR Previous)]**

Where:
- **SAR Previous**: The SAR value of the previous period.
- **AF (Acceleration Factor)**: Starts at 0.02 and increases by 0.02 each time a new extreme point (EP) is reached, up to a maximum of 0.20.
- **EP (Extreme Point)**: The highest high or lowest low in the current trend.

**SAR Calculation Process**:
- In an **uptrend**, the SAR value is calculated by increasing the SAR of the previous period.
- In a **downtrend**, the SAR value is calculated by decreasing the SAR of the previous period.

### **Moving Average Convergence Divergence (MACD)**
The **MACD** is calculated as follows:

- **MACD Line = 12-day EMA - 26-day EMA**
- **Signal Line = 9-day EMA of the MACD Line**
- **MACD Histogram = MACD Line - Signal Line**

Where:
- **EMA**: Exponential Moving Average.
- The most common settings are 12, 26, and 9 days for the EMA.

### **KDJ Indicator**
The **KDJ** indicator is an extension of the Stochastic Oscillator. It includes three lines: **K**, **D**, and **J**.

- **%K = (Current Close - Lowest Low) / (Highest High - Lowest Low) * 100**
- **%D = 3-day SMA of %K**
- **%J = 3 * %K - 2 * %D**

Where:
- **Lowest Low**: The lowest low over a specific period (usually 14 days).
- **Highest High**: The highest high over a specific period (usually 14 days).
- **SMA**: Simple Moving Average.

### **Relative Strength Index (RSI)**
The **RSI** is calculated using the following formula:

- **RSI = 100 - [100 / (1 + RS)]**

Where:
- **RS (Relative Strength) = Average Gain / Average Loss**
- **Average Gain**: The average of all positive price changes over a specific period (typically 14 days).
- **Average Loss**: The average of all negative price changes over the same period.

**RSI Calculation Process**:
1. Calculate the **Average Gain** and **Average Loss** over the initial 14 periods.
2. Continue to smooth the averages as new data comes in.
3. Compute the **RS** and then use the RSI formula. 

These formulas are widely used in technical analysis for identifying trends, reversals, and potential entry/exit points in trading.