## 1. Introduction

### Transitioning to Factor-Based Models

In this lesson, we shift our focus from simply optimizing portfolios based on a basket of stocks to understanding the underlying drivers of returns and risk. Previously, we treated the mean and standard deviation of log returns as fixed numbers. However, in reality, these are not just numbers we can look up; they are uncertain and often noisy.

To address this, we will:
- **Avoid Explicit Return Estimates**: Explicitly estimating returns leads to noisy predictions and unnecessary trading, which incurs costs.
- **Focus on Drivers**: Instead of direct return estimates, we'll concentrate on the underlying **drivers of mean returns** (alpha factors) and **drivers of volatility** (risk factors).

### Understanding and Creating Factors

A **factor** is a numerical value assigned to each stock in a portfolio that has the potential to predict an aspect of future stock performance. Factors are the backbone of quantitative portfolio management. They provide signals that guide where and how much to invest in different stocks.

In this lesson, you will:
- **Learn What a Factor Is**: Factors help in identifying the driving forces behind stock movements.
- **Standardize Factors**: We'll show you how to normalize factors so they can be interpreted as weights for a theoretical portfolio.
- **Use Zipline**: You'll get hands-on experience with Zipline, an open-source Python library for back-testing trading algorithms. This experience will prepare you for using custom libraries in professional environments.

By the end of this lesson, you'll have implemented your first factor in code, setting the foundation for more advanced factor-based portfolio optimization throughout the module.

## 2. Example of a Momentum Factor

Let's explore how a factor works using a **momentum factor** as an example.

#### Hypothesis: 
We hypothesize that the **one-year return** of a stock can provide a signal about its future returns over the next few days. 

#### Steps to Create a Factor:

1. **Collect Price Data**: Gather price data for stocks within your stock universe (a selected group of stocks).
2. **Calculate Returns**: For each stock, calculate the percent change between today's price and the price from one year ago.
3. **Repeat Over Time**: Do this calculation for multiple days to create a time series of one-year returns for each stock.

This collection of one-year returns across different stocks over time is what we refer to as a **factor**. It represents a potential signal that can inform how we allocate weights to each stock in a portfolio and whether to take a long (buy) or short (sell) position.

#### Using the Factor: A Comparison Example

Let's illustrate this with a simple comparison between two stocks: **Apple** and **NVIDIA**.

- **Apple**:
  - On August 3rd, 2018: Price = $208 per share.
  - One year earlier (August 3rd, 2017): Price = $156 per share.
  - **One-year return** = \(\frac{208 - 156}{156} \approx 0.33\) (or 33%).

- **NVIDIA**:
  - On August 3rd, 2018: Price = $252 per share.
  - One year earlier (August 3rd, 2017): Price = $166 per share.
  - **One-year return** = \(\frac{252 - 166}{166} \approx 0.52\) (or 52%).

So, for August 3rd, 2018:
- **Apple's factor value** = 0.33
- **NVIDIA's factor value** = 0.52

#### Interpretation and Action:
Given our hypothesis that a higher factor value suggests better future returns:
- **NVIDIA** (factor = 0.52) might have higher expected returns than **Apple** (factor = 0.33) in the near future.
  
One way to act on this signal is to:
- **Allocate more capital to NVIDIA** (higher positive factor value).
- **Allocate less capital to Apple** (lower positive factor value).

If a stock had a **negative factor value**, you might consider **shorting** that stock, betting that its price will decline.

This simple example demonstrates how a momentum factor can be used to guide investment decisions by comparing the relative performance of stocks based on historical return data.

## 3. Standardizing a Factor

When working with factors, it's crucial to standardize them to ensure that they are comparable and interpretable within a portfolio. The goal is to transform raw factor values into a set of weights that meet two specific conditions:

1. **Sum of Weights Equals Zero**: This ensures that the portfolio is market-neutral, meaning that it doesn't have an inherent bias towards either long or short positions.
2. **Sum of Absolute Values Equals One**: This keeps the portfolio's total exposure normalized, ensuring that the factor doesn't dominate the portfolio by scaling up excessively.

#### Steps to Standardize a Factor

Let's go through the process of standardizing a factor using a simple example with three stocks (A, B, and C). Here's how it works:

1. **De-mean the Factor Values**:
    - **Calculate the Mean**: 
        - Add up the raw factor values for all stocks.
        - Divide the sum by the number of stocks to get the mean.
    - **Subtract the Mean**:
        - For each stock, subtract the calculated mean from its raw factor value.
        - This process is called **de-meaning** because it centers the factor values around zero.
    - **Result**: The sum of these adjusted values (de-meaned values) should now be zero.

2. **Re-scale the Factor Values**:
    - **Calculate the Scalar**:
        - Find the sum of the absolute values of the de-meaned factor values.
    - **Divide by the Scalar**:
        - For each stock, divide the de-meaned factor value by the scalar.
        - This step ensures that the sum of the absolute values of these rescaled factors equals one.

3. **Final Verification**:
    - **Sum of Values**: Confirm that the sum of the standardized values equals zero.
    - **Sum of Absolute Values**: Check that the sum of the absolute values equals one.

#### Example Walkthrough

Imagine three stocks, A, B, and C, with the following raw factor values (e.g., one-year returns):
- **A**: 0.2
- **B**: 0.3
- **C**: 0.5

**Step 1: De-mean the Values**
- **Calculate the Mean**: 
  \[
  \text{Mean} = \frac{0.2 + 0.3 + 0.5}{3} = \frac{1.0}{3} \approx 0.333
  \]
- **De-mean Each Value**:
  \[
  A_{\text{de-meaned}} = 0.2 - 0.333 \approx -0.133
  \]
  \[
  B_{\text{de-meaned}} = 0.3 - 0.333 \approx -0.033
  \]
  \[
  C_{\text{de-meaned}} = 0.5 - 0.333 \approx 0.167
  \]

**Step 2: Re-scale the Values**
- **Calculate the Scalar**:
  \[
  \text{Scalar} = | -0.133 | + | -0.033 | + | 0.167 | = 0.133 + 0.033 + 0.167 = 0.333
  \]
- **Re-scale Each Value**:
  \[
  A_{\text{standardized}} = \frac{-0.133}{0.333} \approx -0.4
  \]
  \[
  B_{\text{standardized}} = \frac{-0.033}{0.333} \approx -0.1
  \]
  \[
  C_{\text{standardized}} = \frac{0.167}{0.333} \approx 0.5
  \]

**Step 3: Verify the Results**
- **Sum of Standardized Values**:
  \[
  -0.4 + (-0.1) + 0.5 = 0
  \]
- **Sum of Absolute Values**:
  \[
  | -0.4 | + | -0.1 | + | 0.5 | = 1.0
  \]

With these steps, you've successfully standardized the raw factor values, making them suitable for further analysis and comparison with other factors.

---

*Bonus Question: Why were the normal distribution and the raw factor unhappy about being standardized?*

Because they thought it was "de-meaning!" 😄

## 4. Why Demeaning Factors Matters: Creating a Dollar Neutral Portfolio

When you demean a factor, you're preparing it to help construct a **dollar neutral** portfolio. Let's break down why this is important and how it works.

#### **1. The Purpose of Demeaning a Factor**
- **Demeaning** involves subtracting the mean of a factor's values across all stocks, which ensures that the sum of these values is zero.
- This is crucial because it allows us to build a portfolio where the total value of long positions equals the total value of short positions, creating a **dollar neutral portfolio**.

#### **2. The Importance of Dollar Neutrality**
- **Market Movement**: Market movement refers to the general trend in stock prices across a market (e.g., upward or downward).
  - A **long-only portfolio** tends to move with the market.
  - A **short-only portfolio** tends to move against the market.
- **Long-Short Portfolio**: By holding both long and short positions, a portfolio can be designed to minimize exposure to the overall market movement.
- **Dollar Neutral Portfolio**:
  - This is a special case of a long-short portfolio where the total dollar value of long positions equals the total dollar value of short positions.
  - Such a portfolio is **market neutral** or at least close to it, meaning its performance is less influenced by the overall market.

#### **3. The Role of Beta**
- **Beta** measures a stock's sensitivity to market movements. In theory, if a stock has a Beta of 1, it moves in tandem with the market.
- By constructing a dollar neutral portfolio, we assume that, on average, the Beta of the stocks is around 1. This assumption helps to ensure that the portfolio is relatively market neutral.

#### **4. Portfolio Weights and Notional Value**
- **Portfolio Weights**: These represent the proportion of the portfolio's total value that is allocated to each stock.
- **Notional Value**: This is the total dollar value of the portfolio.
  - For example, if a portfolio's notional value is $100 million and a stock has a weight of 0.01, the portfolio allocates $1 million to that stock.
- **Dollar Neutral Example**:
  - Suppose you have a portfolio with two stocks:
    - Stock A with a weight of 0.01 results in a **long position** of $1 million.
    - Stock B with a weight of -0.01 results in a **short position** of -$1 million.
  - The total positions add up to zero, making the portfolio dollar neutral.

#### **5. Market Neutrality and Its Goal**
- **Market Neutrality**: The primary goal of a dollar neutral portfolio is to minimize the portfolio's exposure to overall market movements. By focusing on the stock-specific returns (i.e., the alpha), we aim to test the factor's predictive power without the market's influence.

#### **Conclusion**
- **Demeaning** is essential for building dollar neutral portfolios, which in turn helps achieve market neutrality. This allows quants to isolate and test the effectiveness of a factor without the confounding effects of general market movements.

This understanding is foundational for creating robust trading strategies that focus on the predictive power of individual factors rather than on market trends.

## 5. Dollar Neutral Portfolios: Demeaning Weights for Balance

In this part, we'll dive deeper into how to transform a portfolio into a **dollar neutral** portfolio by demeaning the weights of its stocks. This ensures that the portfolio isn't tilted in favor of either long or short positions.

#### **1. Zero Investment Portfolios**
- **Theoretical Dollar Neutral Portfolio**: 
  - In theory, a dollar neutral portfolio doesn't require any cash to create. It's often referred to as a **zero investment portfolio** in academic contexts.
  - In reality, you'd have to consider transaction costs, margin costs for shorting, and timing differences, but for now, we ignore these factors to focus on the concept itself.

#### **2. Visualizing Dollar Neutrality**
- **Initial Portfolio Weights**: 
  - Imagine a portfolio with two stocks, Stock A and Stock B, both with positive weights.
  - On a balancing scale, this portfolio would tilt towards the positive side because both stocks contribute to a net long position, meaning it's not dollar neutral.

- **Relative Difference**:
  - The key point to note is the **relative difference** between the two stocks, which is the weight of Stock A minus the weight of Stock B. This difference is crucial when adjusting the portfolio.

#### **3. Adjusting to Dollar Neutral**
- **Shifting Weights**:
  - To make the portfolio dollar neutral, imagine shifting the weights of both stocks towards the negative side (i.e., short positions). 
  - The goal is to adjust the weights until the scale is balanced—this means the sum of the weights equals zero, achieving dollar neutrality.

- **Maintaining Relative Differences**:
  - During this adjustment, the **relative difference** between the weights of Stock A and Stock B remains unchanged. This ensures that the fundamental relationship between the two stocks in the portfolio is preserved, even as we neutralize the dollar value.

#### **4. The Demeaning Process**
- **Subtracting the Mean**:
  - The technique used to shift the weights is to **subtract the mean** of the weights from each individual weight.
  - This process is known as **demeaning** the portfolio weights, and it effectively balances the portfolio by ensuring the sum of all adjusted weights is zero.

#### **5. Result: A Balanced Portfolio**
- **Balanced Portfolio**:
  - After demeaning the weights, the portfolio becomes dollar neutral. This means the total dollar amount of long positions equals the total dollar amount of short positions, effectively neutralizing the portfolio against market-wide movements.

### **Conclusion**
By demeaning the portfolio weights, you create a dollar neutral portfolio, which is a balanced, market-neutral setup. This allows you to focus on the performance of individual stocks relative to each other, rather than being swayed by overall market trends. This is a crucial step in evaluating the predictive power of your factors and refining your trading strategies.

## 6. Leverage and Rescaling Weights

In this section, we delve into the concepts of **leverage** and the **leverage ratio** and explore why rescaling portfolio weights so that the sum of their absolute values equals one is crucial for achieving a leverage ratio of one.

#### **1. What is Leverage?**
- **Leverage Defined**: 
  - Leverage involves borrowing funds to invest in assets, with the goal of amplifying potential returns.
  - In physics, leverage refers to the use of a lever to amplify force. In finance, leverage amplifies potential gains (and losses) on an investment.

- **Mechanics of Leverage**:
  - If you invest without leverage, the percentage change in your investment equals the percentage change in the asset's value.
  - When you use leverage, you're essentially using borrowed funds to increase the size of your investment. This can magnify your returns.

#### **2. Leverage in Long/Short Portfolios**
- **Borrowing in Long/Short Portfolios**:
  - In a long/short portfolio, leverage can be achieved by borrowing cash or by shorting stocks.
  - When you short a stock, you borrow shares and sell them, planning to buy them back later. The cash received from shorting can then be used to buy other assets in the portfolio.

- **Impact of Leverage**:
  - **Without Leverage**: 
    - Assume an initial capital of $100,000. If the stock price increases by 10%, the portfolio value increases by $10,000, representing a 10% return on the initial investment.
  - **With Leverage**: 
    - Start with $100,000 and borrow an additional $100,000, giving you $200,000 to invest. If the stock price increases by 10%, the portfolio value increases by $20,000. This represents a 20% return on the initial capital of $100,000.

  - **Summary**: The use of leverage amplifies the returns (and risks) relative to the initial capital. A 10% increase in stock price results in a 20% return on the initial investment when leverage is used.

#### **3. The Leverage Ratio and Rescaling Weights**
- **Leverage Ratio**:
  - The **leverage ratio** is the ratio of the total value of the assets in the portfolio to the initial capital. In the example above, with $200,000 invested and $100,000 in initial capital, the leverage ratio is 2.

- **Rescaling Weights**:
  - To control the leverage ratio and set it to 1, we rescale the portfolio weights so that the sum of their absolute values equals one.
  - This ensures that the portfolio is balanced and that the leverage is appropriately managed.

### **Conclusion**
By rescaling the portfolio weights, you ensure that the leverage ratio is controlled, usually aiming for a leverage ratio of one. This allows you to manage risk while still taking advantage of the potential benefits of leverage. This step is critical in constructing portfolios that are both balanced and effective in reflecting the desired investment strategy.

## 7. Risks and Benefits of Leverage, and How to Rescale Weights for Leverage Ratio

In this section, we'll explore the double-edged nature of leverage—its potential to amplify both gains and losses—and how to calculate and control the leverage ratio in a portfolio by rescaling weights.

#### **1. The Double-Edged Sword of Leverage**
- **Potential Gains vs. Risks**:
  - **Amplifying Gains**: Leverage allows investors to magnify their returns by borrowing to invest more than their initial capital.
  - **Amplifying Losses**: However, the downside is that losses are also magnified. A 10% drop in stock prices can lead to a 20% loss in a leveraged portfolio, which is twice as much as without leverage.

- **Leverage Isn't Free**: 
  - The saying "there's no such thing as a free lunch" applies here. The benefits of leverage come with the risk of increased losses.

#### **2. Understanding the Leverage Ratio**
- **Leverage Ratio Calculation**:
  - The leverage ratio measures the total exposure of a portfolio relative to its initial capital (notional).
  - **Formula**: 
    \[
    \text{Leverage Ratio} = \frac{\text{Sum of Absolute Values of Long and Short Positions}}{\text{Notional (Initial Capital)}}
    \]
  
  - **Example**:
    - If a portfolio has $1 million in long positions and no shorts, with an initial capital of $1 million, the leverage ratio is:
      \[
      \text{Leverage Ratio} = \frac{1,000,000}{1,000,000} = 1
      \]
    - If the portfolio instead has $2 million in longs and $1 million in shorts with the same initial capital, the leverage ratio is:
      \[
      \text{Leverage Ratio} = \frac{2,000,000 + 1,000,000}{1,000,000} = 3
      \]

#### **3. Rescaling Weights to Achieve a Leverage Ratio of 1**
- **Rescaling Process**:
  - To achieve a leverage ratio of 1, the sum of the absolute values of the portfolio weights should equal 1. 
  - **Steps**:
    1. **Calculate the Sum of Absolute Values**: Add up the absolute values of all weights in the portfolio.
    2. **Divide Each Weight by This Sum**: Rescale each weight by dividing it by the sum of absolute values.

  - **Example**:
    - Consider a portfolio with weights of -0.5, 0.3, and 0.2. The sum of absolute values is:
      \[
      | -0.5 | + | 0.3 | + | 0.2 | = 1
      \]
      The leverage ratio is 1, so no rescaling is needed.
    - If the weights are -1, 0.6, and 0.4, the sum of absolute values is:
      \[
      | -1 | + | 0.6 | + | 0.4 | = 2
      \]
      To achieve a leverage ratio of 1, divide each weight by 2:
      \[
      \text{Rescaled Weights} = \left[ \frac{-1}{2}, \frac{0.6}{2}, \frac{0.4}{2} \right] = [-0.5, 0.3, 0.2]
      \]

### **Conclusion**
By rescaling weights to ensure the leverage ratio equals 1, you balance the portfolio's exposure relative to its initial capital. This controlled use of leverage allows you to manage risk while optimizing potential returns, striking a balance between risk and reward.

## 8. Overview For Standardizing A Factor

### 1. **De-mean the Factor Values (Dollar Neutrality)**

Given a vector of factor values \( f = [f_1, f_2, \dots, f_n] \) for \( n \) stocks:

1. **Calculate the Mean**:
   \[
   \mu = \frac{1}{n} \sum_{i=1}^{n} f_i
   \]
   This is the average of the factor values.

2. **Subtract the Mean**:
   \[
   f'_i = f_i - \mu \quad \text{for all } i = 1, 2, \dots, n
   \]
   The new vector \( f' = [f'_1, f'_2, \dots, f'_n] \) will have a mean of zero:
   \[
   \sum_{i=1}^{n} f'_i = 0
   \]
   This ensures that the portfolio is dollar neutral.

### 2. **Rescale the Factor Values (Leverage Ratio of One)**

Given the de-meaned factor values \( f' \):

1. **Calculate the Sum of Absolute Values**:
   \[
   S = \sum_{i=1}^{n} |f'_i|
   \]
   This is the total magnitude of all the positions.

2. **Rescale the Factor Values**:
   \[
   w_i = \frac{f'_i}{S} \quad \text{for all } i = 1, 2, \dots, n
   \]
   The new vector \( w = [w_1, w_2, \dots, w_n] \) is now scaled so that:
   \[
   \sum_{i=1}^{n} |w_i| = 1
   \]
   This ensures that the portfolio's leverage ratio is one.

### Example

Let's say we have 3 stocks with the following factor values:

\[
f = [0.4, 0.2, -0.1]
\]

1. **Calculate the Mean**:
   \[
   \mu = \frac{0.4 + 0.2 - 0.1}{3} = \frac{0.5}{3} \approx 0.1667
   \]

2. **Subtract the Mean**:
   \[
   f' = [0.4 - 0.1667, 0.2 - 0.1667, -0.1 - 0.1667] = [0.2333, 0.0333, -0.2667]
   \]

3. **Calculate the Sum of Absolute Values**:
   \[
   S = |0.2333| + |0.0333| + |-0.2667| = 0.2333 + 0.0333 + 0.2667 = 0.5333
   \]

4. **Rescale the Factor Values**:
   \[
   w = \left[\frac{0.2333}{0.5333}, \frac{0.0333}{0.5333}, \frac{-0.2667}{0.5333}\right] = [0.4375, 0.0625, -0.5]
   \]

   These weights now satisfy:
   \[
   \sum_{i=1}^{3} |w_i| = |0.4375| + |0.0625| + |-0.5| = 1
   \]
   And:
   \[
   \sum_{i=1}^{3} w_i = 0.4375 + 0.0625 - 0.5 = 0
   \]
   
This example shows how to convert raw factor values into standardized portfolio weights that are dollar neutral and have a leverage ratio of one.

## 9. Zipline Pipeline

### 1. Introduction to Zipline Pipeline

- **Zipline**: An open-source algorithmic trading simulator.
- **Pipeline**: A sequence of data operations used to filter and rank stocks based on certain criteria. It is useful because it automates the selection process from a large universe of stocks.

### 2. **Loading Data in Zipline**

To use Zipline, you first need to load data using a **data bundle**.

- **Data Bundle**: A packaged dataset that has been ingested into Zipline.
- **Example**:
  ```python
  from zipline.data.bundles import load
  from zipline.utils.calendars import get_calendar
  
  bundle = 'eod-quotemedia'
  data = load(bundle)
  ```

### 3. **Building the Pipeline**

A pipeline can include **screens**, **factors**, and **filters**.

#### 3.1 **Screen**

- A **screen** is a filter that selects stocks based on criteria. 
- Example: A screen selecting the top 10 stocks by average dollar volume over the past 60 days.

  ```python
  from zipline.pipeline import Pipeline
  from zipline.pipeline.factors import AverageDollarVolume
  
  pipeline = Pipeline(
      screen=AverageDollarVolume(window_length=60).top(10)
  )
  ```

#### 3.2 **Factors and Filters**

- **Factor**: A function that returns a numerical value for each stock at a particular time.
- **Filter**: A function that returns a Boolean value (True/False) for each stock.

  Example:
  ```python
  from zipline.pipeline.factors import SimpleMovingAverage
  
  # Factor: 15-day mean closing price
  mean_close_15 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=15)
  
  # Filter: Stocks with 15-day average closing price > $100
  price_filter = mean_close_15 > 100
  
  # Add to pipeline
  pipeline.add(mean_close_15, 'mean_close_15')
  pipeline.add(price_filter, 'price_filter')
  ```

### 4. **Running the Pipeline**

- A **Pipeline Engine** is needed to execute the pipeline.

  ```python
  from zipline.pipeline import engine
  from zipline.pipeline.data import USEquityPricing
  
  engine = SimplePipelineEngine(
      get_loader=USEquityPricingLoader(),
      calendar=get_calendar('NYSE')
  )
  
  result = engine.run_pipeline(pipeline, start_date, end_date)
  ```

### 5. **Visualizing the Pipeline**

- Zipline's `Pipeline` class has a feature to visualize the pipeline structure using a diagram.

  ```python
  pipeline.show_graph()
  ```

### **Math Explanation**

#### 1. **Screening Stocks**: 
   - **Top \( n \) stocks by average dollar volume**:
     \[
     \text{Top Stocks} = \text{sort}( \frac{1}{T} \sum_{t=1}^{T} \text{Volume}(t) \times \text{Price}(t) ) \text{, take top } n
     \]

#### 2. **Factor (Simple Moving Average)**:
   - **SMA of 15 days** for closing prices:
     \[
     \text{SMA}_{15}(i) = \frac{1}{15} \sum_{t=0}^{14} \text{Close Price}(i, t)
     \]

#### 3. **Filter (Price Threshold)**:
   - **Boolean Filter**:
     \[
     \text{Price Filter} = \text{True if } \text{SMA}_{15}(i) > 100, \text{ else False}
     \]

### **Conclusion**

This lesson demonstrated how to set up and run a Zipline pipeline, which allows you to efficiently screen, filter, and rank stocks for algorithmic trading. You'll learn to automate this process with pipelines, creating a powerful tool for systematic trading strategies.