## 1. What Is Optimization

### Understanding Optimization

Optimization is all about finding the "best" solution according to some criteria. In the context of portfolios, this usually means finding the portfolio with the **highest return** for a given level of risk (volatility) or the **lowest risk** for a given level of return.

### Maximization vs. Minimization

- **Maximization**: Finding the maximum value of a function (e.g., maximizing returns).
- **Minimization**: Finding the minimum value of a function (e.g., minimizing risk).

It's worth noting that any maximization problem can be turned into a minimization problem by optimizing the negative of the function. For example, maximizing `f(x)` is the same as minimizing `-f(x)`.

### A Simple Example: Quadratic Function

Let's explore a basic example: finding the minimum of the quadratic function:

\[
Y = (X - 1)^2 + 1
\]

This is a parabola, a U-shaped curve. Our goal is to find the value of \(X\) that makes \(Y\) as small as possible.

#### Visualizing the Function

The function \(Y = (X - 1)^2 + 1\) can be visualized as a parabola. Here's how it looks:

```python
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (x - 1)**2 + 1

# Create a range of x values
x = np.linspace(-2, 4, 400)
y = f(x)

# Plot the function
plt.plot(x, y, label=r'$Y = (X - 1)^2 + 1$')
plt.title('Quadratic Function')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
```

### Finding the Minimum

To find the minimum of the function, notice that the curve has a unique lowest point. This point corresponds to where the derivative (slope) of the function equals zero.

#### Derivative of the Function

The derivative of the function gives us the slope at any point on the curve:

\[
\frac{dY}{dX} = 2(X - 1)
\]

We set this derivative equal to zero to find the point where the slope is zero (the minimum):

\[
2(X - 1) = 0
\]

Solve for \(X\):

\[
X = 1
\]

So, the minimum value of \(Y\) occurs at \(X = 1\).

### Verification

Substitute \(X = 1\) back into the original function to find the corresponding \(Y\) value:

\[
Y = (1 - 1)^2 + 1 = 0 + 1 = 1
\]

So, the minimum value of the function is \(Y = 1\) at \(X = 1\).

### Key Takeaways

- **Optimization** involves finding the best solution under given constraints.
- **Maximization** problems can be converted into **minimization** problems.
- For simple functions, the minimum or maximum can be found by setting the derivative equal to zero and solving for the variable.
  
### Looking Ahead

This example is a simple optimization problem where we can find an exact solution. In more complex scenarios, especially in portfolio optimization, we may have multiple variables, constraints, and objectives. Solving these problems will require more advanced methods, such as linear programming, quadratic programming, or using numerical algorithms.

Stay tuned as we explore these more advanced optimization techniques!

## 2. Optimization With Constraints

Let's dive into the concepts you've introduced, using both mathematical insights and clear examples to make it easier to understand how to solve optimization problems with constraints, especially in the context of portfolio optimization.

### Key Concepts in Optimization with Constraints

#### 1. **Objective (or Cost) Function**
   - The function you want to optimize (minimize or maximize).
   - In portfolio optimization, this could represent something like the risk or variance of a portfolio that you want to minimize.

#### 2. **Optimization Variable**
   - The variable(s) you're trying to find the best value for.
   - In portfolio optimization, this typically refers to the weights of the different assets in the portfolio.

#### 3. **Constraints**
   - These are the conditions that the solution must satisfy.
   - **Equality Constraints**: Conditions of the form \(f(x) = 0\).
   - **Inequality Constraints**: Conditions of the form \(g(x) \leq 0\).
   - Example: If you're optimizing portfolio weights, a constraint might be that all weights sum to 1 (equality constraint), or that no weight can be negative (inequality constraint).

#### 4. **Feasibility**
   - A point (solution) is **feasible** if it satisfies all the constraints.
   - The problem is **feasible** if at least one feasible solution exists.
   - It’s **infeasible** if no solution satisfies all constraints.

### Example of a Constrained Optimization Problem

Consider the quadratic function:

\[
f(x) = (x - 1)^2 + 1
\]

Without constraints, we already found that the minimum occurs at \(x = 1\), where \(f(x) = 1\).

#### Adding a Constraint

Now, let's introduce a constraint: \(x \leq 0\). This constraint limits the region where we can look for the solution.

**Graphically**, this means that we’re only interested in the portion of the function where \(x \leq 0\). 

#### Finding the New Minimum

Given the constraint \(x \leq 0\), the smallest value of \(f(x)\) in this region occurs at the boundary of the constraint:

\[
x = 0 \quad \text{(since \(x > 0\) is not allowed by the constraint)}
\]

Substituting \(x = 0\) into the objective function:

\[
f(0) = (0 - 1)^2 + 1 = 1^2 + 1 = 2
\]

So, the new minimum value, considering the constraint, is 2, occurring at \(x = 0\).

### Convex Optimization

#### What is a Convex Function?
   - A function is convex if, for any two points on the curve, the line segment between them lies above or on the curve.
   - **Example**: The function \(f(x) = (x - 1)^2 + 1\) is convex because it curves upwards everywhere.

#### Why Convexity Matters
   - **Convex Optimization Problem**: When the objective function is convex and the constraints are either convex inequalities or linear equalities, the problem is easier to solve.
   - A key property: Any local minimum is also a global minimum.

### Convex Optimization Problem Example

Let’s define a convex optimization problem:

Objective function:

\[
f(x) = \frac{1}{2}x^2 + 2x + 1
\]

Constraint:

\[
x \geq -3
\]

1. **Is the function convex?**
   - Yes, because the second derivative of \(f(x)\) (which is 1) is positive, indicating an upward curve.

2. **Solution Without Constraints**:
   - The derivative of \(f(x)\) is \(f'(x) = x + 2\).
   - Set \(f'(x) = 0\): 
     \[
     x + 2 = 0 \implies x = -2
     \]
   - Substituting \(x = -2\) into \(f(x)\):
     \[
     f(-2) = \frac{1}{2}(-2)^2 + 2(-2) + 1 = 2 - 4 + 1 = -1
     \]
   - So, the minimum value is \(-1\) at \(x = -2\).

3. **Solution with Constraint \(x \geq -3\)**:
   - Since \(-2\) satisfies the constraint \(x \geq -3\), it remains the optimal solution.

### Summary

- **Objective Function**: The function you want to optimize.
- **Optimization Variable**: The variable you adjust to optimize the objective function.
- **Constraints**: Conditions that restrict the values of the optimization variables.
- **Convex Problems**: Easier to solve because any local minimum is also a global minimum.

In portfolio optimization, convex optimization plays a crucial role because we often deal with quadratic functions (representing risk) and linear constraints (like budget constraints). The convex nature of these problems ensures that solutions can be efficiently found and are globally optimal.

## 3. Two-Asset Portfolio Optimization

### Derivation of Optimal Weights in a Two-Asset Portfolio

In portfolio optimization, the goal is to find the optimal weights for the assets in a portfolio such that the portfolio has the lowest possible variance (risk) for a given level of expected return. Let's work through the problem using a portfolio with two assets, Stock A and Stock B.

#### 1. **Objective Function: Portfolio Variance**
The portfolio variance \( \sigma_P^2 \) is a measure of the risk of the portfolio, and it's given by the formula:

\[
\sigma_P^2 = x_A^2\sigma_A^2 + x_B^2\sigma_B^2 + 2x_Ax_B\sigma_A\sigma_B\rho_{r_A r_B}
\]

Where:
- \( x_A \) and \( x_B \) are the weights of Stock A and Stock B in the portfolio.
- \( \sigma_A \) and \( \sigma_B \) are the standard deviations (volatility) of Stock A and Stock B.
- \( \rho_{r_A r_B} \) is the correlation between the returns of Stock A and Stock B.

Our objective is to **minimize** the portfolio variance \( \sigma_P^2 \).

#### 2. **Constraint**
The weights of the assets must sum to 1:

\[
x_A + x_B = 1
\]

This constraint ensures that the entire portfolio is allocated between Stock A and Stock B.

#### 3. **Substitution into the Objective Function**
We can express \( x_B \) in terms of \( x_A \) using the constraint:

\[
x_B = 1 - x_A
\]

Substituting this into the objective function:

\[
\sigma_P^2 = x_A^2\sigma_A^2 + (1-x_A)^2\sigma_B^2 + 2x_A(1-x_A)\sigma_A\sigma_B\rho_{r_A r_B}
\]

This is now a function of a single variable, \( x_A \).

#### 4. **Finding the Optimal Weight \( x_A \)**
To find the value of \( x_A \) that minimizes the portfolio variance, we take the derivative of \( \sigma_P^2 \) with respect to \( x_A \) and set it equal to zero:

\[
\frac{\mathrm{d} (\sigma_P^2)}{\mathrm{d} x_A} = 2x_A\sigma_A^2 - 2\sigma_B^2(1-x_A) + 2\sigma_A\sigma_B\rho_{r_A r_B}[-x_A + (1-x_A)]
\]

Simplifying:

\[
0 = 2x_A\sigma_A^2 + 2\sigma_B^2x_A - 2\sigma_B^2 + 2\sigma_A\sigma_B\rho_{r_A r_B}[1 - 2x_A]
\]

Further simplification gives:

\[
x_A[\sigma_A^2 + \sigma_B^2 - 2\sigma_A\sigma_B\rho_{r_A r_B}] = \sigma_B^2 - \sigma_A\sigma_B\rho_{r_A r_B}
\]

Finally, solving for \( x_A \):

\[
x_A = \frac{\sigma_B^2 - \sigma_A\sigma_B\rho_{r_A r_B}}{\sigma_A^2 + \sigma_B^2 - 2\sigma_A\sigma_B\rho_{r_A r_B}}
\]

#### 5. **Finding \( x_B \)**
From the constraint:

\[
x_B = 1 - x_A
\]

This gives us the weight of Stock B in the portfolio.

#### 6. **Expected Portfolio Return**
If you want to calculate the expected return of the portfolio \( \mu_P \), it can be found using the weighted sum of the individual expected returns:

\[
\mu_P = \mu_A x_A + \mu_B x_B
\]

Where:
- \( \mu_A \) and \( \mu_B \) are the expected returns of Stock A and Stock B, respectively.

#### 7. **Second-Order Condition Check**
To ensure that the solution for \( x_A \) corresponds to a minimum, you should check the second derivative of the objective function. If the second derivative is positive, then \( x_A \) indeed corresponds to a minimum.

### Visualization Example
To get an intuitive feel for this, assume specific values:
- \( \sigma_A = 0.1 \) (standard deviation of Stock A)
- \( \sigma_B = 0.05 \) (standard deviation of Stock B)
- \( \rho_{r_A r_B} = 0.25 \) (correlation between Stock A and Stock B returns)

Plotting the portfolio variance \( \sigma_P^2 \) as a function of \( x_A \), you'd see a parabolic curve where the lowest point represents the minimum variance and gives you the optimal weights \( x_A \) and \( x_B \).

### Conclusion
This derivation allows you to find the optimal weights for a two-asset portfolio, minimizing the portfolio's risk while considering the relationship between the assets' returns. This approach can be extended to more complex portfolios with multiple assets, using similar principles and more advanced optimization techniques.

## 4. Formulating Portfolio Optimization Problems

### Formulating Portfolio Optimization Problems

In portfolio optimization, the problem can be formulated in various ways depending on the objective and constraints. Let's explore different approaches to set up a portfolio optimization problem.

#### 1. Common Constraints

When setting up a portfolio optimization problem, several constraints are commonly applied:

- **No Short Selling:** If short selling is not allowed, the portfolio weights \( x_i \) must be non-negative. This can be expressed as:
  \[
  0 \leq x_i \leq 1, \quad i = 1, 2, \dots, n
  \]
- **Sector Limits:** You might want to limit the exposure to certain sectors. For instance, if you want to limit investments in the biotech sector, you would impose a constraint like:
  \[
  x_{\text{biotech1}} + x_{\text{biotech2}} + x_{\text{biotech3}} \leq M
  \]
  where \( M \) represents the maximum percentage of the portfolio allocated to biotech companies.
- **Constraint on Portfolio Return:** If you aim to achieve a minimum portfolio return, you can add a constraint:
  \[
  \mathbf{x}^\mathrm{T} \mathbf{\mu} \geq r_{\text{min}}
  \]
  where \( r_{\text{min}} \) is the minimum acceptable portfolio return.

#### 2. Maximizing Portfolio Return

Instead of minimizing variance, another approach is to maximize portfolio returns. This method makes sense when the goal is to achieve the highest return possible while managing risk by imposing a variance constraint.

- **Objective:**
  \[
  \text{minimize:} \quad -\mathbf{x}^\mathrm{T} \mathbf{\mu}
  \]
- **Constraint:**
  \[
  \mathbf{x}^\mathrm{T} \mathbf{P}\mathbf{x} \leq p
  \]
  where \( p \) is the maximum permissible portfolio variance.

#### 3. Maximizing Portfolio Return and Minimizing Portfolio Variance

A more comprehensive approach combines both objectives—maximizing returns and minimizing variance—by introducing a tradeoff parameter \( b \).

- **Objective:**
  \[
  \text{minimize:} \quad -\mathbf{x}^\mathrm{T} \mathbf{\mu} + b\mathbf{x}^\mathrm{T} \mathbf{P}\mathbf{x}
  \]
  where \( b \) represents how much return you are willing to sacrifice for each unit of variance you take on.

#### 4. A Math Note: The L2-Norm

The L2-norm, also known as the Euclidean norm, is a way to measure the distance between two vectors. It is calculated as:
\[
d = \sqrt{(a_x - b_x)^2 + (a_y - b_y)^2 + (a_z - b_z)^2} = \left \| \mathbf{a} - \mathbf{b} \right \|_2
\]
In two dimensions, this reduces to the familiar Pythagorean theorem:
\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

#### 5. Minimizing Distance to a Set of Target Weights

One optimization approach is to minimize the distance between the current portfolio weights and a set of target weights \( \mathbf{x}^* \) using the L2 norm.

- **Objective:**
  \[
  \text{minimize:} \quad \left \| \mathbf{x} - \mathbf{x}^* \right \|_2
  \]
  where \( \mathbf{x}^* \) represents the target portfolio weights.

#### 6. Tracking an Index

If you want to track an index while minimizing portfolio variance, you can set up an objective function that includes both terms. The tradeoff between tracking the index and minimizing variance is controlled by a parameter \( \lambda \).

- **Objective:**
  \[
  \text{minimize:} \quad \mathbf{x}^\mathrm{T}\mathbf{P}\mathbf{x} + \lambda \left \| \mathbf{x} - \mathbf{q} \right \|_2
  \]
  where \( \mathbf{q} \) represents the index weights, and \( \lambda \) is the tradeoff parameter.

These formulations provide a flexible framework for addressing different portfolio optimization problems, allowing you to tailor the setup according to specific objectives and constraints.

## 5. Rebalancing A Portfolio

### Rebalancing a Portfolio

After constructing a portfolio using optimization techniques, your job as a portfolio manager isn't finished. The next crucial step is to regularly monitor and rebalance the portfolio to ensure it stays aligned with your investment goals. Over time, the value of assets changes, which affects the portfolio weights—the proportion of the total investment allocated to each asset. 

#### Why Rebalance?

Rebalancing ensures that your portfolio maintains its desired risk and return profile. For instance, suppose you initially invested 50% in a solar energy company and 50% in a construction company. If the solar energy company's value increases significantly, it might represent 70% of your portfolio. To return to the 50-50 allocation, you would sell some shares of the solar energy company and buy more shares of the construction company.

#### How to Rebalance?

When rebalancing, you essentially re-run the original optimization process using updated data, while keeping the same objective function and constraints. The updated portfolio weights will reflect the current market values of the assets.

#### Costs of Rebalancing

Rebalancing isn't free; it incurs costs, including:

1. **Transaction Costs:** Every trade typically incurs a fee, known as a commission, paid to brokers. These costs can be significant, especially when managing large portfolios. For example, in 2000, the Texas Permanent School Fund spent $120 million on transaction costs while rebalancing a $17.5 billion portfolio.

2. **Taxes:** Capital gains taxes may apply when selling assets that have appreciated in value.

3. **Administrative Costs:** These include the time and labor required to execute the trades.

#### Portfolio Turnover

To estimate the costs associated with rebalancing, we use the concept of **portfolio turnover**, which measures the total magnitude of change in the portfolio’s holdings. Portfolio turnover is calculated as the sum of the absolute changes in the portfolio weights of all assets between two time periods:

\[
\text{Turnover} = \sum_{i=1}^{n} \left| x_i^{\text{new}} - x_i^{\text{old}} \right|
\]

Where \( x_i^{\text{new}} \) and \( x_i^{\text{old}} \) are the new and old weights of asset \( i \), respectively.

#### Annualized Turnover

To calculate annualized turnover:

1. Calculate the turnover for each rebalancing event.
2. Take the average turnover across all events within the timeframe.
3. Multiply this average by the number of rebalancing events per year.

\[
\text{Annualized Turnover} = \frac{\sum_{k=1}^{m} \text{Turnover}_k}{m} \times \text{Events per year}
\]

Where \( m \) is the number of rebalancing events.

Understanding and managing these costs is essential to maintaining a portfolio's efficiency and ensuring that rebalancing doesn't inadvertently erode the portfolio's returns.

## 6. Rebalancing Strategies

### Rebalancing Strategies

Rebalancing a portfolio involves adjusting the weights of assets to maintain a target allocation. This process is crucial for managing risk and ensuring that the portfolio aligns with the investor's goals. But when should you rebalance? There are two main types of events that trigger rebalancing:

1. **Cash Flows**
2. **Changes in Model Parameters**

#### 1. Cash Flows

Cash flows refer to the movement of money into and out of the portfolio. Common sources of cash flows include:

- **Dividends:** Payments received from stocks. If you've shorted a stock, you're required to pay dividends to the stock's owner.
- **Capital Gains:** Increases in asset value that become realized gains when the asset is sold.
- **New Contributions:** Additional investments made into the portfolio.

When cash flows occur, the simplest way to adjust is to buy or sell assets according to the current portfolio weights. However, if some assets have appreciated or depreciated in value, the weights will have shifted from their target allocations. In such cases, you can use cash flows to rebalance the portfolio back to its desired allocation.

#### 2. Changes in Model Parameters

Changes in the underlying parameters of the stock return model, such as expected returns or risk levels, might also prompt rebalancing. These changes don't automatically trigger rebalancing; instead, the portfolio manager must decide if the change is significant enough to justify the costs involved in rebalancing.

For example, corporate actions like mergers or changes in management can affect the model's parameters. If the portfolio manager suspects a parameter change, they will re-estimate the model and determine if rebalancing is necessary by weighing the benefits against the transaction costs.

### Common Rebalancing Strategies

There are several strategies for determining when to rebalance:

#### 1. **Temporal Frequency Rebalancing**

This strategy involves rebalancing at fixed intervals, such as daily, monthly, quarterly, or annually, regardless of changes in portfolio weights. The frequency is often based on the time horizon used in the portfolio's optimization process. For instance, if the portfolio was optimized using monthly data, rebalancing might be performed monthly, as the optimal weights are assumed to be valid for one month.

#### 2. **Threshold-Based Rebalancing**

This strategy triggers rebalancing only when the portfolio weights deviate from the target weights by a certain threshold, such as 1%, 5%, or 10%. Rebalancing under this strategy doesn't occur at fixed intervals but rather when the weights shift beyond the predetermined threshold. This could happen as often as daily or as infrequently as annually.

#### 3. **Combined Strategy**

A combined strategy involves rebalancing on a set schedule but only if the portfolio weights have drifted beyond the threshold. Both criteria must be met for rebalancing to occur:

- **Scheduled Date:** Rebalancing is considered on the pre-determined date.
- **Threshold Condition:** Rebalancing occurs only if the deviation from target weights exceeds the threshold.

If the deviation is below the threshold on the scheduled date, rebalancing won't be performed. Similarly, if the weights drift by more than the threshold before the scheduled date, rebalancing still won't be done until the scheduled date arrives.

### Summary

Choosing the right rebalancing strategy depends on the portfolio's objectives, the investor's risk tolerance, and the associated transaction costs. Temporal frequency rebalancing is straightforward and regular, while threshold-based rebalancing is more responsive to market changes. The combined strategy offers a balanced approach by incorporating both time and weight deviations, ensuring that rebalancing is done efficiently and cost-effectively.

## 7. Limitations

### Limitations of Portfolio Optimization

While portfolio optimization is a powerful tool in finance, it has several practical limitations that need to be considered:

#### 1. **Difficulty in Estimating Mean Returns**

- **Challenge**: Accurately estimating mean returns is notoriously difficult because past returns are often poor indicators of future returns.
- **Workarounds**: 
  - **Alternative Strategies**: Instead of directly estimating returns, one can minimize the difference between the portfolio weights and a set of target weights.
  - **Predictive Substitutes**: Use alternative quantities that are believed to be predictive of future returns as substitutes for direct return estimates.

#### 2. **Issues with Portfolio Variance Estimation**

- **Risk Measurement**: Variance may not always be an adequate measure of risk. For instance, it doesn't capture the asymmetry in the distribution of returns.
- **Example**: Two distributions can have the same mean and standard deviation but very different shapes, particularly in the negative tail, which is crucial for understanding the risk of large negative returns.
- **Alternative Risk Measures**: Consider alternative measures of risk that can better capture the shape of the distribution, especially the downside risk.

#### 3. **Covariance Matrix Estimation Challenges**

- **Complexity**: Estimating a covariance matrix becomes increasingly difficult as the number of assets (n) in the portfolio increases.
- **Problem Size**: The covariance matrix has \( n \times n \) elements, which means the problem size grows rapidly with the number of assets.
- **Data Requirements**: A large amount of historical data is required to estimate the covariance matrix accurately. For example, estimating a covariance matrix for 50 assets might require at least five years of daily data.
- **Noise Handling**: Estimates are noisy, and one way to manage this is by using ranks instead of raw values to focus on relative magnitudes.

#### 4. **Turnover and Transaction Costs**

- **Turnover Penalties**: Including a term in the objective function that penalizes turnover can reduce the frequency of trading, making the portfolio less sensitive to noise.
- **Robust Optimization**: This method accounts for the confidence intervals of estimates, making the optimization process more resilient to uncertainty.

#### 5. **Temporal Validity of Optimized Weights**

- **Dynamic Market Conditions**: Optimized portfolio weights are only valid as long as the input parameters (like expected returns and covariances) remain accurate.
- **No Built-in Adaptation**: Traditional optimization methods lack mechanisms to adapt to changes in market conditions over time, potentially leading to suboptimal decisions.

#### 6. **Conflicting Predictions Across Time Horizons**

- **Single-Period Framework**: Traditional portfolio optimization often considers only a single time period, which doesn't accommodate conflicting predictions across different time horizons.
- **Example**: A model might predict positive returns over a one-day horizon but negative returns over a one-month horizon. In a single-period framework, it’s unclear how to reconcile these conflicting predictions.
- **Multi-Period Optimization**: This approach involves planning trades over several periods while optimizing for future trades based on current information. The actual trades are executed only for the first period, helping to avoid decisions that could be detrimental in the future.

#### 7. **Modeling Transaction Costs**

- **Ambiguity**: Accurately modeling transaction costs is difficult. They are often assumed to be proportional to turnover, but this is a simplification.
- **Optimization Inclusion**: Transaction costs can be included in the optimization problem as a constraint or a term to minimize within the objective function.

#### 8. **Factor-Based Models**

- **Practical Alternative**: Factor-based models are often more practical in addressing some of the weaknesses of traditional portfolio optimization, such as difficulties in estimating means, variances, and covariances.

### Summary

Portfolio optimization, while valuable, has several limitations that practitioners must navigate. These include challenges in estimating mean returns, dealing with the complexities of covariance matrices, and managing transaction costs. Alternative strategies like robust optimization, multi-period optimization, and factor-based models can help address these issues, providing more practical solutions in real-world scenarios. Future lessons will delve deeper into these topics, offering more detailed strategies for overcoming these challenges.