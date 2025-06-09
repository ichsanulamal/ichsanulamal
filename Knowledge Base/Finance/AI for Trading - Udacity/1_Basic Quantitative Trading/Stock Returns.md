## 1. Returns

### Understanding Stock Market Data: Measuring Changes in Value

When analyzing stock market data, we're often dealing with time series of stock prices. While the fluctuations in these prices might be interesting on their own, especially if you're curious about how a company is performing, the primary concern for most investors is how these changes affect the value of their investments. In other words, we want to measure how much our investment has increased or decreased over time.

#### Key Metrics for Measuring Price Changes

There are several ways to quantify changes in stock prices over time. Let's explore two common metrics:

1. **Price Difference**:
   \[
   \Delta P_t = P_t - P_{t-1}
   \]
   - **Explanation**: This represents the simple difference between the price of the stock at time \( t \) and its price at the previous time \( t-1 \). For example, if you’re looking at monthly prices, this could be the difference between the stock price this month and last month.

2. **Percentage Return (or Raw Return)**:
   \[
   R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{\Delta P_t}{P_{t-1}}
   \]
   - **Explanation**: This is the difference in price normalized by the initial price at time \( t-1 \). It shows the relative change in price, which is often more useful than the absolute change because it allows for comparison across different investments or time periods.

#### Example: Comparing Investments

Let's say you make two different investments and want to compare their performances:

- **Investment 1**:
  - Initial investment: $1,000
  - Value after one month: $1,050
  - **Price difference**: \( \Delta P = 1050 - 1000 = 50 \)
  - **Percentage return**: \( R = \frac{50}{1000} = 0.05 \) or 5%

- **Investment 2**:
  - Initial investment: $5,000
  - Value after one month: $5,300
  - **Price difference**: \( \Delta P = 5300 - 5000 = 300 \)
  - **Percentage return**: \( R = \frac{300}{5000} = 0.06 \) or 6%

Although the absolute gains were different ($50 vs. $300), the percentage returns allow you to compare the performance of the two investments directly. Here, the second investment had a higher return (6% vs. 5%), meaning it performed better relative to its initial value.

### Why Use Percentage Returns?

Percentage returns are particularly important because they "normalize" the data, making it easier to compare different investments regardless of their initial values. This normalization is also essential for many statistical and machine learning models, which often require data on a similar scale to function properly.

### Summary

- **Price difference** tells you how much the price has changed in absolute terms.
- **Percentage return** shows you the relative change, which is more useful for comparing different investments or time periods.

Understanding these metrics is crucial for making informed investment decisions and for conducting more advanced analyses using statistical or machine learning techniques.

## 2. Log Returns

### Understanding Logarithmic Returns in Finance

In finance, particularly among quantitative analysts, there's a quantity that's frequently used and closely related to the raw return—this is the **logarithmic return** (or log return). While the raw return gives a straightforward percentage change in price, the log return offers a different perspective with some unique advantages.

#### Defining Raw and Log Returns

First, let's recall the formulas:

1. **Raw Return** \( r_t \):
   \[
   r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
   \]
   This represents the percentage change in price from one time period to the next.

2. **Logarithmic Return** \( R_t \):
   \[
   R_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
   \]
   This is the natural logarithm of the ratio of the current price \( P_t \) to the previous price \( P_{t-1} \).

#### Converting Between Raw and Log Returns

To convert between raw return \( r_t \) and log return \( R_t \), let's look at the relationship between them:

1. **From Raw Return to Log Return**:
   - Start with the raw return formula:
     \[
     r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
     \]
   - Add 1 to both sides:
     \[
     1 + r_t = \frac{P_t}{P_{t-1}}
     \]
   - Take the natural logarithm of both sides to get the log return:
     \[
     R_t = \ln(1 + r_t)
     \]

2. **From Log Return to Raw Return**:
   - Start with the log return formula:
     \[
     R_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
     \]
   - Exponentiate both sides to solve for \( \frac{P_t}{P_{t-1}} \):
     \[
     e^{R_t} = \frac{P_t}{P_{t-1}}
     \]
   - Subtract 1 to revert to the raw return:
     \[
     r_t = e^{R_t} - 1
     \]

These equations show that you can easily switch between raw and log returns, depending on which form is more convenient for analysis.

#### Why Use Log Returns?

Log returns have several appealing properties, which make them useful in financial analysis:

1. **Approximation for Small Returns**:
   - When returns are small, the log return \( R_t \) is approximately equal to the raw return \( r_t \). Mathematically:
     \[
     \ln(1 + r_t) \approx r_t
     \]
   - This approximation works because the function \( \ln(1 + x) \) is nearly linear when \( x \) is small. The graph of \( \ln(1 + x) \) is tangent to the line \( y = x \) at \( x = 0 \), meaning that for small \( x \), the difference between \( \ln(1 + x) \) and \( x \) is minimal.

2. **Additivity**:
   - Unlike raw returns, log returns are additive over time. If you want to calculate the total return over multiple periods, you can simply sum the log returns for each period:
     \[
     R_{\text{total}} = R_1 + R_2 + \dots + R_n
     \]
   - This additivity simplifies many calculations and is especially useful in continuous time finance models.

3. **Normal Distribution**:
   - Financial returns are often assumed to be normally distributed in many models. Log returns, rather than raw returns, tend to be more normally distributed, making them better suited for statistical analysis.

#### Visualization

To better understand the relationship between the logarithm and raw return, consider the function \( y = \ln(1 + x) \). This function intersects the origin (0,0) and has a slope of 1 at \( x = 0 \). This means that near \( x = 0 \), the function \( \ln(1 + x) \) behaves almost like the line \( y = x \). Here's a visualization to help:

- **At \( x = 0 \)**: The function \( \ln(1 + x) \) and the line \( y = x \) overlap, meaning that for very small values of \( x \), \( \ln(1 + x) \approx x \).
- **As \( x \) increases**: The curve \( \ln(1 + x) \) deviates from the line \( y = x \), but for small values (like typical stock returns), the approximation holds well.

#### Summary

- **Log returns** are useful in finance due to their additivity and better distributional properties.
- **Raw returns** can be converted to log returns using \( R_t = \ln(1 + r_t) \), and vice versa using \( r_t = e^{R_t} - 1 \).
- **For small returns**, log returns closely approximate raw returns, simplifying analysis without losing accuracy.

## 3. Distribution Of Stock Prices

### Understanding How Daily Stock Prices Evolve

When analyzing how daily stock prices change, it's essential to recognize that these changes are often small and cumulative, reflecting the concept of **compounding**. Let's break down how this process works and how it leads to specific statistical distributions.

#### Compounding and Stock Prices

Suppose a stock price starts at \( P_0 \), and each day it changes by a small percentage, which we refer to as the **daily return** \( r_i \). The price at any time \( t \) can be expressed as the product of these small daily changes:

\[
P_t = P_0 \times (1 + r_1) \times (1 + r_2) \times \dots \times (1 + r_t)
\]

This equation shows that the price at time \( t \) is the initial price \( P_0 \) compounded by each day's return.

#### Taking the Logarithm of Price

To simplify analysis, we often take the natural logarithm of both sides of the equation:

\[
\ln(P_t) = \ln(P_0) + \ln(1 + r_1) + \ln(1 + r_2) + \dots + \ln(1 + r_t)
\]

Here, \( \ln(P_t) \) represents the logarithm of the stock price at time \( t \), and the sum on the right-hand side is the sum of the logarithms of the daily returns plus the logarithm of the initial price \( P_0 \).

For convenience, we can rewrite this as:

\[
\ln(P_t) - \ln(P_0) = \sum_{i=1}^{t} \ln(1 + r_i)
\]

Since \( P_0 \) is a constant (the initial price), \( \ln(P_t) - \ln(P_0) \) represents the cumulative effect of all the daily returns from time 0 to \( t \).

#### The Central Limit Theorem (CLT) and Stock Prices

Now, let's bring in the **Central Limit Theorem (CLT)**, a fundamental concept in probability. The CLT states that the sum of a large number of independent and identically distributed (i.i.d.) random variables will tend to follow a normal distribution, regardless of the original distribution of the variables, as the number of variables becomes large.

If we assume:
- The daily returns \( r_i \) are independent and identically distributed (i.i.d.).
- Each \( \ln(1 + r_i) \) is a random variable that comes from the same underlying distribution.

Then, according to the CLT, the sum of \( \ln(1 + r_i) \) over a long period will follow a **normal distribution**.

Thus, we have:

\[
\ln(P_t) - \ln(P_0) \sim \mathcal{N}(\mu, \sigma^2)
\]

This means that the difference \( \ln(P_t) - \ln(P_0) \) is normally distributed with some mean \( \mu \) and variance \( \sigma^2 \).

Since \( \ln(P_0) \) is a constant, \( \ln(P_t) \) itself is normally distributed:

\[
\ln(P_t) \sim \mathcal{N}(\mu', \sigma^2)
\]

#### Introducing the Log-Normal Distribution

A crucial concept here is the **log-normal distribution**:

- If a random variable \( Y \) is normally distributed, i.e., \( Y \sim \mathcal{N}(\mu, \sigma^2) \), then \( e^Y \) follows a **log-normal distribution**.
- In our context, if \( \ln(P_t) \) is normally distributed, then the stock price \( P_t \) (which is \( e^{\ln(P_t)} \)) is **log-normally distributed**.

The log-normal distribution is characterized by:
- **Right skewness**: The distribution is skewed to the right, meaning there is a longer tail on the right side of the distribution.
- **Non-negativity**: The distribution doesn't go below zero, which aligns with the fact that stock prices can't be negative.

#### Practical Considerations

While assuming that stock prices are log-normally distributed is a common and convenient model, it's important to remember that:
- **Log-normality is an assumption**: The real-world distribution of stock prices or returns may deviate from this model.
- **Use with caution**: While this assumption can simplify calculations and theoretical models, it's crucial not to confuse it with the actual distribution of stock prices, which can be more complex.

### Summary

- **Daily price evolution**: Stock prices evolve through small daily returns, leading to a compounded effect over time.
- **Logarithmic transformation**: Taking the log of the price simplifies the product of returns into a sum, which is easier to analyze.
- **Central Limit Theorem**: The sum of log returns tends to follow a normal distribution, assuming independence and identical distribution.
- **Log-normal distribution**: Since the log of prices is normally distributed, the prices themselves follow a log-normal distribution, which is right-skewed and non-negative, aligning well with actual stock price behavior.

Understanding these concepts provides a foundation for modeling and analyzing stock prices and returns in quantitative finance.