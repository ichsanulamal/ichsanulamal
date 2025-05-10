## 1. Intro 

### Introduction to Mean Reversion and Co-integration in Trading

In this lesson, we'll explore two key properties of financial assets: **mean reversion** and **co-integration**. Understanding these properties is essential for grasping certain trading strategies, including **Pairs Trading** and the broader concept of **Mean Reversion Trading**. Let's begin by defining these concepts.

---

### What is Mean Reversion?

**Mean reversion** refers to a statistical property of a time series where values tend to move back toward a long-term average or mean over time. In the context of stock prices, mean reversion implies that if a stock price deviates significantly from its historical average, it may eventually return to that average.

**Example**:
- Suppose a stock typically trades around $50, but due to some market fluctuations, it drops to $40. If the stock is mean-reverting, you might expect it to eventually climb back toward $50.
  
  \[
  \text{Expected Price Movement} = \text{Current Price} + \left( \text{Mean Price} - \text{Current Price} \right)
  \]

However, there is always a risk:
- The stock may not revert to its historical mean and could instead settle at a new lower price or continue to decline.

### Mean Reversion Applied to Pairs of Stocks

While mean reversion can be applied to a single stock, it's more commonly used in conjunction with **Pairs Trading**, where two stocks are considered together. This approach relies on the assumption that two stocks are economically linked and hence their prices tend to move together.

#### Economically Linked Companies:
- **Same Industry:** Two companies might operate in the same industry, such as two major banks.
- **Same Region:** Companies operating in the same geographical region.
- **Similar Products:** Companies offering similar products or targeting the same customer base.

When the stock prices of these two companies deviate from their typical relationship, traders might assume this divergence is temporary and bet on the prices reverting to their historical relationship.

**Example**:
- Imagine Company A and Company B, both tech firms, usually have closely related stock prices. If Company A's stock suddenly drops while Company B's remains stable, a trader might buy Company A's stock expecting it to rise and short Company B's stock expecting it to fall or remain stable.

### Trading Strategy: Pairs Trading

**Pairs Trading** is a strategy that involves taking a position in two correlated stocks:

1. **Identify a Pair:** Choose two stocks that historically move together.
2. **Monitor Divergence:** Watch for significant deviations in their price relationship.
3. **Execute Trades:**
   - If Stock A falls below its expected price relative to Stock B, buy Stock A.
   - Simultaneously, short Stock B.
4. **Close the Position:** When the prices revert to their historical relationship, close both positions to capture the profit.

### Generalization: Mean Reversion Trading

Beyond pairs trading, **Mean Reversion Trading** can apply to any asset that exhibits mean-reverting behavior. The general steps are:

1. **Identify the Mean:** Determine the long-term average price of the asset.
2. **Monitor Price:** Watch for deviations from this mean.
3. **Execute Trades:** Buy when the price falls significantly below the mean, or short when it rises significantly above the mean.
4. **Close the Position:** When the price moves back toward the mean, close the position.

### Conclusion

In this lesson, we've introduced the concepts of mean reversion and co-integration, laying the foundation for understanding trading strategies like Pairs Trading and Mean Reversion Trading. We'll explore these strategies in more detail in the following sections.

## 2. Mean Reversion

### Detailed Exploration of Mean Reversion Using the Drift and Volatility Model

Let's delve deeper into the concept of mean reversion and introduce the **Drift and Volatility model** to describe it mathematically. To make this concept easier to grasp, we'll use an analogy of a boat drifting in the ocean.

---

### Stock Price Movements and Moving Averages

When we observe a stock's price over time, we can plot its movements against a **moving average**. The moving average smooths out short-term fluctuations and highlights longer-term trends. What we often see is that when the stock price deviates significantly from this moving average—whether by increasing or decreasing—the price tends to "revert" back toward the moving average. This behavior is what we call **mean reversion**.

### The Drift and Volatility Model

To describe the mean-reverting process mathematically, we use the **Drift and Volatility model**. This model captures how a stock's price changes over time by considering both a **long-term trend** (drift) and **random fluctuations** (volatility).

#### The Boat Analogy

Imagine a boat floating on the ocean:

- **Drift:** The boat is carried by the ocean current. This current represents the long-term trend or average movement of the stock price, which changes slowly and steadily over time.
- **Volatility:** As the boat drifts, it gets bumped by fish, dolphins, or even whales. These random bumps represent the unpredictable fluctuations in the stock price.

Now let's translate this analogy into a mathematical model.

### The Mathematical Model

The **Drift and Volatility model** can be represented as follows:

\[
dp_t = a \cdot p_t \cdot dt + \sigma \cdot p_t \cdot \epsilon \cdot \sqrt{dt}
\]

Where:

- \( dp_t \) is the change in the stock price over a small time interval \( t \).
- \( p_t \) is the current stock price at time \( t \).
- \( a \) is the **drift coefficient**, representing the long-term average rate of return.
- \( dt \) is the small change in time.
- \( \sigma \) is the **volatility coefficient**, representing the standard deviation of the stock's returns.
- \( \epsilon \) is a random noise factor that represents the random bumps (like fish or whales) the boat encounters.
- \( \sqrt{dt} \) accounts for the fact that volatility increases with the square root of time.

#### Breaking Down the Equation

1. **Drift Term (\( a \cdot p_t \cdot dt \)):**
   - This term represents the long-term, average direction of the stock price movement. It's like the ocean current that moves the boat steadily over time.
   - The drift depends on the current price \( p_t \) and the time interval \( dt \).
   - It indicates a predictable, slow change in the stock price.

2. **Volatility Term (\( \sigma \cdot p_t \cdot \epsilon \cdot \sqrt{dt} \)):**
   - This term represents the random, unpredictable changes in the stock price, much like the bumps from fish, dolphins, or whales.
   - The volatility term depends on:
     - **Current Price \( p_t \)**: Higher prices can lead to larger absolute changes.
     - **Standard Deviation \( \sigma \)**: Measures the magnitude of the random changes.
     - **Random Noise \( \epsilon \)**: Captures the randomness of the market.
     - **Square Root of Time \( \sqrt{dt} \)**: Reflects how randomness accumulates over time.

### Intuition Behind the Model

- **Calm Market (Small \( \sigma \)):** When the market is calm, the bumps (volatility) are small—like encountering a few fish. The boat (stock price) drifts smoothly along the current (drift term).
- **Volatile Market (Large \( \sigma \)):** In a volatile market, the bumps are larger—like encountering whales. The stock price experiences larger, more erratic changes.

### Conclusion

The **Drift and Volatility model** offers a mathematical framework for understanding how stock prices evolve over time, combining a steady, long-term trend with random short-term fluctuations. By thinking of a boat drifting in the ocean, encountering various bumps along the way, we can visualize how a stock's price might deviate from its moving average but eventually revert back, embodying the concept of mean reversion.

In the next part of this lesson, we'll explore how this model can be applied in practical trading strategies.

## 3. Pairs Trading

### Understanding Pairs Trading: A Detailed Examination

Pairs trading is a market-neutral strategy that leverages the economic link between two companies by taking advantage of the price divergence between their stocks. This strategy is rooted in the concepts of mean reversion and statistical relationships between the stock prices of the two companies.

#### 1. **Economic Links Between Companies**

When two companies have economic ties, their stock prices tend to move in a similar manner. For example, consider:

- **Company A**: Sells frozen green peas.
- **Company B**: Sells frozen carrots.

Since frozen peas and carrots are often sold together, both companies are likely to see their sales move in tandem. If sales rise, both companies benefit, and their stock prices should, in theory, increase together. However, due to market conditions or company-specific news, the prices of these stocks might occasionally diverge.

#### 2. **Concept of Divergence and Mean Reversion**

When the stock prices of these two economically linked companies diverge—meaning one stock price increases while the other decreases—this could present a trading opportunity based on the assumption of **mean reversion**. The idea is that the divergence is temporary and that the stock prices will eventually revert to their historical relationship.

#### 3. **Executing a Pairs Trade**

Pairs trading involves two key actions:

- **Going Long**: Buy the stock that is priced relatively low.
- **Going Short**: Sell (short) the stock that is priced relatively high.

**Example**:
- **Stock A**: Priced lower than usual.
- **Stock B**: Priced higher than usual.
  
You would buy Stock A (long position) and sell Stock B (short position). The expectation is that Stock A will rise and Stock B will fall or stay constant, leading to a convergence in their prices. Once the prices converge, you close your positions—sell Stock A and buy back Stock B (cover your short)—to realize a profit.

#### 4. **Risk Management and Closing Positions**

Pairs trading isn't risk-free. There are scenarios where the prices continue to diverge rather than converge. In such cases, traders must decide when to close their positions to cut losses. The timing for closing positions depends on historical trends and the trader's risk tolerance.

**Time Horizons**:
- **Longer Term**: Some pairs may diverge and converge over weeks or months.
- **Shorter Term**: Day traders might look for divergences and convergences within hours or even minutes, focusing on smaller price movements.

#### 5. **Advantages of Pairs Trading**

One of the main benefits of pairs trading is that it reduces exposure to broader market movements:

- **Market Neutrality**: By going long one stock and short another, pairs trading minimizes the impact of overall market trends. For instance, if a negative jobs report causes a market-wide decline, both stocks might drop. However, the focus is on the relative price difference between the two stocks rather than their absolute prices.

#### 6. **Understanding Spread and Hedge Ratio**

To effectively manage a pairs trade, traders need to calculate two important metrics: the **spread** and the **hedge ratio**.

**Hedge Ratio**: 
- The hedge ratio defines the proportion of the two stocks in the trade to achieve a neutral position, meaning that movements in one stock should ideally offset movements in the other.
  
**Calculation Methods**:
1. **Price Ratio Method**: 
   \[
   \text{Hedge Ratio} = \frac{\text{Price of Stock B}}{\text{Price of Stock A}}
   \]

2. **Linear Regression Method**:
   - Run a regression with Stock A as the independent variable (X) and Stock B as the dependent variable (Y). The **regression coefficient** gives the hedge ratio. This method accounts for historical price movements and may provide a more stable hedge ratio than the price ratio method.

**Spread Calculation**:
- Once the hedge ratio is determined, the **spread** between the two stocks can be calculated as:
  \[
  \text{Spread} = \text{Price of Stock B} - (\text{Hedge Ratio} \times \text{Price of Stock A})
  \]

This spread is analogous to the **residual** in regression analysis, representing the difference between the observed price of Stock B and its expected price based on Stock A's price.

#### 7. **Application of Spread and Hedge Ratio**

In pairs trading, the goal is to monitor the spread. If the spread widens (i.e., the stocks diverge), it may indicate a potential trading opportunity. Conversely, when the spread narrows (i.e., the stocks converge), it may be time to close the trade and lock in profits.

### Conclusion

Pairs trading is a sophisticated strategy that leverages the economic links between two companies, their stock price correlations, and the principles of mean reversion. By understanding and calculating the hedge ratio and spread, traders can create a market-neutral position that reduces exposure to broader market trends while potentially profiting from the relative movements of the two stocks. This strategy requires careful analysis and timing, but when executed well, it can be a powerful tool in a trader's arsenal.

## 4. Finding Pairs To Trade

### Identifying Good Pairs for Trading

In pairs trading, finding the right pairs of stocks is crucial. The goal is to identify pairs of companies with strong economic links that will cause their stock prices to move together. However, these links can take various forms, some obvious and others more subtle. Let's explore how to identify these connections and evaluate their suitability for pairs trading.

#### 1. **Identifying Economic Links Between Companies**

**Same Sector and Country:**
- Companies in the same sector and country are often subject to similar economic conditions, regulations, and market trends.
- **Example**: Two major banks in the United States. Both would be influenced by U.S. monetary policy, interest rates, and economic growth.

**International Trade Relations:**
- Companies across different countries but in the same industry might be linked through international trade relations.
- **Example**: U.S. and Chinese steel companies. Political decisions, such as tariffs or trade agreements, can affect the steel industry in both countries similarly.

**Supply Chain Relationships:**
- A supplier and a customer within the same supply chain can also be economically linked.
- **Example**: A textile manufacturer and a clothing retailer. A drop in clothing sales might first hit the retailer and then ripple back to the textile supplier as orders decrease.

**Different Time Zones:**
- Companies in similar industries but different time zones may show correlated movements with a time lag.
- **Example**: A pharmaceutical company in India and a similar company in Germany. If international demand for medicines increases, the Indian company might see its stock rise first, followed by the German company a few hours later due to time zone differences.

#### 2. **Exploiting Time Lags in Pairs Trading**

**Time Lag Opportunities:**
- Time lags between movements of economically linked stocks can be exploited in pairs trading. 
- If you observe Stock A (e.g., the Indian pharmaceutical company) moving up due to positive news, you might anticipate that Stock B (e.g., the German pharmaceutical company) will follow suit once the market in its time zone opens.

**Trading Strategy:**
- **Step 1**: Monitor the movement of Stock A.
- **Step 2**: If Stock A moves up, predict that Stock B will move similarly.
- **Step 3**: Place your trade after Stock A's movement but before Stock B reacts.
- **Step 4**: Close the position once Stock B follows the expected movement.

#### 3. **Evaluating the Pair: Calculating the Spread**

Once you've identified a pair of stocks based on their economic links, the next step is to evaluate whether they are good candidates for pairs trading by analyzing the **spread** between their prices.

**Spread Calculation:**
- As previously discussed, the spread is calculated as:
  \[
  \text{Spread} = \text{Price of Stock B} - (\text{Hedge Ratio} \times \text{Price of Stock A})
  \]
- The hedge ratio can be determined using the price ratio or linear regression method.

**Stationarity of the Spread:**
- For a pair to be a good candidate for pairs trading, the spread should be **stationary** over time.
- **Stationarity** means that the spread has a stable mean, variance, and covariance over time. This implies that any deviation from the spread is likely to revert back to the mean, which is crucial for mean-reversion strategies like pairs trading.

**Checking for Stationarity:**
- **Visual Inspection**: Plot the spread over time. If it fluctuates around a constant mean without any trends or volatility changes, it's likely stationary.
- **Statistical Tests**: You can use statistical tests like the Augmented Dickey-Fuller (ADF) test to check for stationarity formally.

#### 4. **Why Stationarity Matters**

- **Mean Reversion**: A stationary spread indicates that the difference between the two stocks' prices tends to revert to a long-term average. This mean-reverting behavior is what pairs trading strategies aim to exploit.
- **Reduced Risk**: Stationary pairs are less likely to experience prolonged divergences, reducing the risk of losses from positions that don't converge.

### Conclusion

Identifying and evaluating pairs for trading requires both an understanding of the economic links between companies and a careful analysis of their price movements. By finding pairs with strong, economically justified connections and verifying that their spread is stationary, you can enhance the likelihood of success in pairs trading. Moreover, exploiting time lags between related stocks can provide additional opportunities for profit.

## 5. Cointegration

### Understanding Cointegration in Stock Pairs

To grasp the relationship between two stocks in financial markets, it's essential to understand the concept of **cointegration**. Cointegration provides insight into whether two time series, like stock prices, move together over time in a consistent manner, despite potential short-term fluctuations.

#### Integrated Time Series

First, let's clarify what it means for a time series to be "integrated of order one" (I(1)). When a stock price series is I(1), it means the series itself is non-stationary—its statistical properties change over time, such as having a trend. However, if we take the difference between consecutive values in the series, we might get a stationary series, one where the statistical properties do not change over time. A stationary series is said to be "integrated of order zero" (I(0)).

#### Cointegration Explained

Now, let's move on to cointegration. Imagine two stocks, X and Y, that are economically linked. If we subtract the price of one stock from the other, we might obtain a new series called the **spread**. If this spread is stationary, we say that X and Y are cointegrated. 

Mathematically, this involves a **hedge ratio** (let's denote it as \(\beta\)). The hedge ratio can be obtained through regression:

\[
Y_t = \alpha + \beta X_t + \epsilon_t
\]

Here, \(Y_t\) is the price of stock Y at time \(t\), \(X_t\) is the price of stock X at time \(t\), \(\alpha\) is the intercept, \(\beta\) is the hedge ratio, and \(\epsilon_t\) is the error term (spread). The spread \(\epsilon_t = Y_t - \beta X_t\) is what we check for stationarity.

If \(\epsilon_t\) (the spread) is stationary, then X and Y are cointegrated. This means that, even if X and Y individually wander over time, their linear combination remains stable, indicating a long-term equilibrium relationship.

#### Cointegration vs. Correlation

It's crucial to distinguish between **cointegration** and **correlation**:

- **Correlation** measures how two stocks move together in the short term. It ranges from -1 (perfect negative correlation) to +1 (perfect positive correlation). For example, a strong positive correlation means when stock A goes up, stock B also goes up.

- **Cointegration**, on the other hand, looks at the long-term relationship. Two stocks can be highly correlated without being cointegrated, meaning they might move together now but could drift apart over time. Conversely, two stocks can be cointegrated but show little short-term correlation.

For example, suppose you invest $100 in both stock A and stock B. If these stocks are cointegrated, the value of these positions will stay roughly equal over time, even if their individual prices fluctuate.

#### Testing for Cointegration

To test if two stocks are cointegrated, we use the **Engle-Granger Test**. This involves two key steps:

1. **Find the Hedge Ratio**: Perform a regression analysis to estimate the hedge ratio (\(\beta\)).
   
2. **Test the Spread for Stationarity**: Calculate the spread (\(\epsilon_t = Y_t - \beta X_t\)) and use the **Augmented Dickey-Fuller (ADF) Test** to check for stationarity.

The ADF test provides a **p-value**. If the p-value is small (typically 0.05 or less), we can reject the null hypothesis of a unit root and conclude that the spread is stationary. Thus, the two stocks are cointegrated.

#### Practical Application: Pairs Trading

In **pairs trading**, investors look for pairs of stocks that are cointegrated. The strategy involves taking a long position in one stock and a short position in the other, betting that any divergence in their prices will converge back to the equilibrium dictated by their cointegrated relationship.

### Key Takeaways

- **Integrated Series**: Stock prices are often integrated of order one (I(1)), but their differences can be stationary (I(0)).
- **Cointegration**: When two stocks have a stationary spread, they are said to be cointegrated, indicating a long-term equilibrium relationship.
- **Cointegration vs. Correlation**: Cointegration refers to a long-term relationship, whereas correlation refers to short-term movements.
- **Engle-Granger Test**: Used to test for cointegration, involving regression for the hedge ratio and the ADF test for spread stationarity.
  
Understanding these concepts can help you make more informed decisions in trading strategies like pairs trading, where identifying cointegrated pairs is key.

## 6. ADF and roots

### ADF and Roots of the Characteristic Equation

#### Understanding the ADF Test in Mathematical Terms

The **Augmented Dickey-Fuller (ADF) test** is commonly described as a test for the presence of a **unit root** in a time series. To delve deeper into the math, let's start with the concept of an **AR(p) model**:

\[
y_t = \beta_1 y_{t-1} + \beta_2 y_{t-2} + \dots + \beta_p y_{t-p} + \epsilon_t
\]

Here, \(y_t\) represents the value of the series at time \(t\), and \(\epsilon_t\) is white noise (random error).

#### The Characteristic Equation

We can rearrange this AR(p) model by moving all terms involving \(y\) to the left side:

\[
y_t - \beta_1 y_{t-1} - \beta_2 y_{t-2} - \dots - \beta_p y_{t-p} = \epsilon_t
\]

Next, we set \(\epsilon_t = 0\) to obtain what is known as the **characteristic equation**:

\[
y_t - \beta_1 y_{t-1} - \beta_2 y_{t-2} - \dots - \beta_p y_{t-p} = 0
\]

#### Backward Shift Notation

To solve for the roots of the characteristic equation, we introduce **backward shift notation**:

\[
B^n y_t = y_{t-n}
\]

For example, \(y_{t-1}\) can be replaced with \(B^1 y_t\), and \(y_{t-2}\) with \(B^2 y_t\). Rewriting the characteristic equation using backward shift notation:

\[
y_t - \beta_1 B y_t - \beta_2 B^2 y_t - \dots - \beta_p B^p y_t = 0
\]

Now, we can factor out \(y_t\):

\[
y_t (1 - \beta_1 B - \beta_2 B^2 - \dots - \beta_p B^p) = 0
\]

The term inside the parentheses is the characteristic polynomial, and the roots of this polynomial tell us about the stationarity of the series.

#### Examples

1. **Random Walk (AR(1) Model with \(\beta = 1\))**:
   - Consider an AR(1) model: \( y_t = y_{t-1} + \epsilon_t \)
   - The characteristic equation is: \( y_t - y_{t-1} = 0 \)
   - Using backward shift notation: \( y_t - B y_t = 0 \)
   - Factor out \(y_t\): \( y_t(1 - B) = 0 \)
   - The root is \( B = 1 \), which indicates a unit root, meaning the series is **not stationary**.

2. **Stationary AR(1) Model with \(\beta = \frac{1}{2}\)**:
   - The model is: \( y_t = \frac{1}{2} y_{t-1} + \epsilon_t \)
   - The characteristic equation is: \( y_t - \frac{1}{2} y_{t-1} = 0 \)
   - In backward shift notation: \( y_t - \frac{1}{2} B y_t = 0 \)
   - Factor out \(y_t\): \( y_t(1 - \frac{1}{2} B) = 0 \)
   - Solving for \(B\): \( B = 2 \), which is greater than 1, indicating the series is **stationary**.

For series with more than one lag (higher-order AR models), there can be multiple roots. If all roots are greater than 1, the series is stationary.

#### The ADF Test Hypotheses

- **Null Hypothesis (H0)**: The series has a unit root (i.e., it is not stationary).
- **Alternative Hypothesis (H1)**: The series is stationary (i.e., all roots are greater than 1).

If the ADF test gives a **p-value** of 0.05 or less, we reject the null hypothesis and conclude that the series is stationary.

### Engle-Granger Test for Cointegration

The **Engle-Granger Test** is used to determine if two time series are cointegrated. The test involves:

1. **Calculating the Hedge Ratio**: Run a regression of one series on the other:

   \[
   y_t = \beta x_t + \epsilon_t
   \]

   Here, \(\beta\) is the hedge ratio.

2. **Testing for Stationarity**: Compute the residuals \( z_t = y_t - \beta x_t \) and apply the ADF test to check if \(z_t\) is stationary. If it is, the series \(x_t\) and \(y_t\) are cointegrated.

Understanding these concepts requires a solid grasp of both time series analysis and the underlying mathematics. However, the key takeaway is that the ADF test is a tool to determine whether a series is stationary by examining the roots of its characteristic equation, and the Engle-Granger Test helps identify cointegration between two series by checking the stationarity of their spread.

## 7. Clustering Stocks

### Finding Cointegrated Pairs from a Universe of Stocks

When looking to identify cointegrated pairs of stocks from a large universe, such as those listed in the S&P 500, comparing every possible pair would be inefficient and prone to false positives. Instead, it's essential to partition the universe into meaningful groups to focus the search. Here's how you can approach this:

#### 1. **Grouping by Sector or Industry**
   - **Traditional Approach**: One common method is to group stocks based on their sector or industry. For example, stocks in the technology sector are likely to share common economic drivers, making them good candidates for cointegration analysis.
   - **Limitations**: This approach, while effective, is widely used. It might overlook more subtle relationships between stocks that aren't immediately apparent by sector alone.

#### 2. **Clustering Using Unsupervised Machine Learning**
   - **Why Clustering?**: To find meaningful but less obvious relationships between stocks, you can use **clustering algorithms**—a type of unsupervised machine learning. These algorithms group similar time series together based on their historical price movements, which can reveal hidden patterns or relationships not captured by sector-based grouping.
   
   - **How Clustering Works**: 
     - **Input**: The historical time series data for each stock, such as daily closing prices.
     - **Algorithm**: You can use clustering algorithms like **K-Means**, **Hierarchical Clustering**, or **DBSCAN**.
     - **Output**: The algorithm groups the stocks into clusters where the time series are more similar to each other than to those in other clusters.
   
   - **Process**:
     1. **Normalize the Data**: Before clustering, it's essential to normalize or standardize the stock prices to ensure that the algorithm compares the shapes of the series, not just the absolute values.
     2. **Choose a Clustering Algorithm**: 
        - **K-Means**: Groups stocks into a pre-defined number of clusters. It works well when you know how many clusters to expect.
        - **Hierarchical Clustering**: Builds a tree of clusters, allowing you to decide the number of clusters based on a distance threshold.
        - **DBSCAN**: Identifies clusters based on density, which can help find clusters of varying shapes and sizes.
     3. **Evaluate Clusters**: After clustering, evaluate the clusters to ensure they are meaningful. Stocks in the same cluster should exhibit similar price behavior.
   
   - **Post-Clustering Analysis**: After forming clusters, you can perform cointegration tests, such as the Engle-Granger Test, on pairs within the same cluster. This step involves:
     - **Testing for Cointegration**: Within each cluster, test pairs of stocks to identify those that are cointegrated. This ensures that the pairs selected have a long-term equilibrium relationship.
     - **Fundamental Analysis**: Beyond statistical tests, analyze the fundamental economic relationships between the stocks in the cointegrated pairs. This helps to ensure that the statistical relationship is grounded in an economic rationale.

### Steps to Find Cointegrated Pairs Using Clustering

1. **Data Preparation**: 
   - Collect historical price data for all stocks in the universe (e.g., S&P 500).
   - Normalize the data to focus on the shape and pattern of time series rather than absolute price levels.

2. **Apply Clustering**:
   - Choose a clustering algorithm based on your dataset and goals.
   - Cluster the stocks into groups where each group contains stocks with similar price movements.

3. **Analyze Clusters**:
   - Identify and validate the clusters.
   - Within each cluster, use the Engle-Granger Test to find pairs of stocks that are cointegrated.

4. **Fundamental Relationship Check**:
   - Review the cointegrated pairs to understand the economic rationale behind their relationship.
   - Ensure that the cointegration is not merely a statistical artifact but reflects a meaningful economic linkage.

5. **Pairs Trading Strategy**:
   - Use the identified cointegrated pairs to implement a pairs trading strategy, where you take a long position in one stock and a short position in the other, expecting their prices to converge over time.

By leveraging clustering, you can efficiently narrow down the search for cointegrated pairs, focusing on those with meaningful relationships, while avoiding spurious correlations that could lead to false positives. This approach combines the power of machine learning with traditional financial analysis to enhance the robustness of pairs trading strategies.

## 8. Trade Pairs Of Stocks

### Defining Thresholds for Spread Divergence in Pairs Trading

In pairs trading, determining when two stocks are diverging from their typical spread is crucial. This divergence signals opportunities to execute trades based on the expectation that the spread will revert to its historical mean. Here’s how you can approach this:

#### 1. **Establishing Thresholds**
   - **Threshold for Wide Spread (Shorting the Spread)**: 
     - When the spread between two stocks is significantly wider than its historical average, it indicates that one stock has increased in price relative to the other. The expectation here is that the spread will decrease in the future, meaning the prices will converge.
     - **Action**: Short the spread. This involves:
       - Shorting the stock that has risen in price relative to the other.
       - Buying the stock that has declined in price relative to the other.
   - **Threshold for Narrow Spread (Going Long the Spread)**:
     - Conversely, when the spread is narrower than usual, it suggests that the prices of the two stocks are closer than their historical norm. The expectation is that the spread will widen again.
     - **Action**: Go long the spread. This involves:
       - Buying the stock that has decreased in price relative to the other.
       - Shorting the stock that has increased in price relative to the other.

   - **Conceptual Simplification**:
     - **Buy Low, Sell High**: Essentially, when the spread is wide, you "sell high" by shorting the overpriced stock and "buy low" by purchasing the underpriced stock. When the spread is narrow, the opposite applies.

#### 2. **Using Z-Score to Define Thresholds**
   - **What is a Z-Score?**
     - The Z-score is a statistical measure that describes how far a data point is from the mean in terms of standard deviations. For pairs trading, it helps in quantifying how much the current spread deviates from its historical average.
     - **Formula**: 
       \[
       Z\text{-score} = \frac{\text{Current Spread} - \text{Mean Spread}}{\text{Standard Deviation of Spread}}
       \]
     - **Interpretation**:
       - A Z-score of +1 indicates that the spread is one standard deviation above the mean.
       - A Z-score of -1 indicates that the spread is one standard deviation below the mean.

   - **Setting the Threshold**:
     - **Wide Spread**: You might decide to short the spread when the Z-score exceeds +2. This suggests the spread is significantly wider than usual.
     - **Narrow Spread**: You might go long the spread when the Z-score falls below -2, indicating the spread is unusually narrow.

#### 3. **Backtesting the Strategy**
   - **Importance of Backtesting**: Before deploying your trading strategy, it’s crucial to test it using historical data. Backtesting helps ensure that the strategy would have been profitable in the past and gives confidence that it might perform well in the future.
   
   - **Steps in Backtesting**:
     1. **Divide the Data**:
        - **Training Set**: Early historical data, used to train your model.
        - **Validation Set**: Data following the training set, used for tuning and optimizing the model.
        - **Test Set**: The most recent data, used to evaluate the final model's performance.
     2. **Training**:
        - Train your model on the training set to understand the relationships between the stocks and the behavior of the spread.
     3. **Validation**:
        - Use the validation set to fine-tune the model, adjusting parameters to improve its predictive accuracy.
     4. **Testing**:
        - Finally, test the model on the test set to evaluate its real-world performance. This step is crucial to avoid overfitting the model to past data.
     5. **Avoiding Data Leakage**:
        - Ensure the test set is only used once the model is fully optimized. Using the test set prematurely can lead to biased results, akin to giving the model information about the future.

By defining clear thresholds based on the Z-score, and rigorously backtesting the strategy, you can improve the robustness of your pairs trading strategy, ensuring it is both statistically sound and practically effective.

## 9. Cointegration with 2 or more stocks

### Understanding the Johansen Test for Cointegration

The Johansen Test is a statistical method used to determine whether a group of stocks are cointegrated. Cointegration refers to a situation where multiple time series, such as stock prices, move together in the long term, even though they might diverge in the short term. The Johansen Test helps identify such relationships and calculates the appropriate weights for a linear combination of these stocks to form a spread that we can use in pairs trading.

#### 1. **Vector Autoregression (VAR)**
   - In time series analysis, a Vector Autoregression (VAR) model helps describe how a stock’s current value depends not only on its past values but also on the past values of other stocks.
   - For two stocks, IBM and GE, the VAR model can be written as:
     \[
     \text{IBM}_t = \mu_{\text{IBM}} + \beta_{1,1} \times \text{IBM}_{t-1} + \beta_{1,2} \times \text{GE}_{t-1} + e_{1,t}
     \]
     \[
     \text{GE}_t = \mu_{\text{GE}} + \beta_{2,1} \times \text{IBM}_{t-1} + \beta_{2,2} \times \text{GE}_{t-1} + e_{2,t}
     \]
   - Using matrix notation, this can be simplified to:
     \[
     \begin{bmatrix}\text{IBM}_t\\ \text{GE}_t\end{bmatrix} = \begin{bmatrix}\mu_{\text{IBM}} \\ \mu_{\text{GE}}\end{bmatrix} + \begin{bmatrix}\beta_{1,1} & \beta_{1,2}\\ \beta_{2,1} & \beta_{2,2} \end{bmatrix}\begin{bmatrix}\text{IBM}_{t-1}\\ \text{GE}_{t-1}\end{bmatrix} + \begin{bmatrix}e_{1,t}\\ e_{2,t}\end{bmatrix}
     \]
   - For ease, we denote the matrix of coefficients as **B** and the vector of stock prices as **x**. The model becomes:
     \[
     x_t = \mu + B x_{t-1} + e_t
     \]

#### 2. **Vector Error Correction Model (VECM)**
   - To make the series stationary (removing trends over time), we look at the timewise difference:
     \[
     \Delta x_t = x_t - x_{t-1}
     \]
   - The VECM is then expressed as:
     \[
     \Delta x_t = \mu + B x_{t-1} + C_1 \Delta x_{t-1} + \dots + C_p \Delta x_{t-p} + e_t
     \]
   - Here, \( B x_{t-1} \) captures the long-term relationship between the stocks, while the other terms describe short-term dynamics.

#### 3. **Rank of Matrix B**
   - The Johansen Test examines the rank of the matrix **B**:
     - **Rank 0**: No cointegration among the stocks.
     - **Rank 1**: A single linear combination of the stocks is stationary, indicating one cointegrated relationship.
     - **Rank 2 or 3**: More complex relationships, with two or three stocks possibly cointegrated.
   - For example, if the test shows a rank of 2 among three stocks, only two stocks are necessary to form a cointegrated pair, and you should test different pairs to find which ones.

#### 4. **Using the Johansen Test Results**
   - The Johansen Test provides the eigenvector corresponding to the largest eigenvalue, which gives the weights to use in forming the spread:
     \[
     w_1 \times \text{stock}_1 + w_2 \times \text{stock}_2 + w_3 \times \text{stock}_3 = \text{spread}
     \]
   - These weights determine the proportion of each stock in the spread. You track this spread to identify opportunities for pairs trading based on temporary deviations from its historical mean.

#### 5. **Summary**
   - The Johansen Test checks for cointegration among a group of stocks and provides the necessary weights to form a spread. This spread is monitored for deviations, offering trading opportunities when the spread diverges and is expected to revert to its mean.

By understanding the Johansen Test, you can effectively identify and trade cointegrated pairs, leveraging the long-term relationships between stocks to capture profits from short-term deviations.