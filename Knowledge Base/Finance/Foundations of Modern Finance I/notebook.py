# ---
# title: "Time Series Data and Models"
# subtitle: "Model Identification and Estimation"
# author: "Paul F. Mende"
# date: "Summer 2021"
# output: 
#   html_notebook:
#   df_print: paged
#   toc: yes
# ---

# ## The right model?

# Making inferences from real-world data and building effective models is a challenging process.  The data rarely fits exactly, and models may stop working.  So it always requires judgment, not just stats and number crunching, in applying modeling and forecasting techniques. For that reason, Monte Carlo simulations provide an excellent testing laboratory for identifcation techniques.  We can be sure that a "right answer" exists, then see which analytics identify it and how much uncertainty remains in a best-case scenario.

# - Given a model, estimate its parameters
# - Given a class of models, determine the best

# ## Order determination:  AR(2) Example

# In[2]:
# Now we'll load packages.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import yfinance as yf

# In[3]:
# Simulate AR(2) process
c_0 = 0.001
c_1 = -0.1
c_2 = 0.4
sigma = 1
Nt = 1000
r = np.zeros(Nt)
z = np.random.normal(size=Nt)

for t in range(2, Nt):
    r[t] = c_0 + c_1 * r[t - 1] + c_2 * r[t - 2] + sigma * z[t]

plt.figure(figsize=(10, 6))
plt.plot(np.cumsum(r))
plt.title('AR(2) Sample Path')
plt.xlabel('Time')
plt.ylabel('r')
plt.grid(True)
plt.show()

# In[4]:
plot_acf(r, title="AR(2) Sample Autocorrelation Function")
plot_pacf(r, title="AR(2) Sample Partial Autocorrelation Function")
plt.show()

# ## Model estimation: AR(2) example

# In[5]:
# Method (1) Numerical estimation using ordinary least squares
y = r[2:]
x1 = r[1:-1]
x2 = r[:-2]

X = np.column_stack([x1, x2])
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

# In[6]:
# Method (2): Using the arima function
model_ar2 = sm.tsa.ARIMA(r, order=(2, 0, 0)).fit()
print(model_ar2.summary())

# In[7]:
# What if we get the order incorrect?
model_ar5 = sm.tsa.ARIMA(r, order=(5, 0, 0)).fit()
print(model_ar5.summary())

# ## Order determination: MA(2) Example

# In[8]:
# Simulate MA(2) process
mu = 0.0
sigma = 1.0
phi_1 = -0.1
phi_2 = 0.4
r = np.zeros(Nt)
z = np.random.normal(size=Nt)

r[0] = mu + sigma * z[0]
r[1] = mu + sigma * z[1] + phi_1 * z[0]
for t in range(2, Nt):
    r[t] = mu + sigma * z[t] + phi_1 * z[t - 1] + phi_2 * z[t - 2]

plt.figure(figsize=(10, 6))
plt.plot(np.cumsum(r))
plt.title('MA(2) Sample Path')
plt.xlabel('Time')
plt.ylabel('r')
plt.grid(True)
plt.show()

# In[9]:
plot_acf(r, title="MA(2) Sample Autocorrelation Function")
plot_pacf(r, title="MA(2) Sample Partial Autocorrelation Function")
plt.show()

# ## Model estimation: MA(2)

# In[10]:
model_ma2 = sm.tsa.ARIMA(r, order=(0, 0, 2)).fit()
print(model_ma2.summary())

# ## Real data is much harder

import yfinance as yf

# Define query parameters
ticker = "TR"
date_first = "1987-12-31"
date_last = "2017-12-31"

# Get the data
TR = yf.download(ticker, start=date_first, end=date_last)

# In[12]:
# Here is what the price looks like over time

plt.plot(TR.index, TR['Adj Close'], label='Adjusted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('TR Adjusted Price 1988-2017')
plt.grid(True)
plt.show()

# In[13]:
# Compute the returns
P = TR['Adj Close']
r = np.diff(np.log(P))
N = len(r)

# The returns can also be stored as a new column in TR.
TR['r'] = np.append([np.nan], r)

# Trim off the first row, which has return NA
TR = TR.dropna()

plt.plot(TR.index, TR['r'], label='Daily Returns')
plt.xlabel('Time')
plt.ylabel('Returns')
plt.title('TR Daily Returns 1988-2017')
plt.grid(True)
plt.show()

# In[14]:
# Is the series stationary?
plt.plot(TR.index, np.random.normal(0, np.std(TR['r']), len(TR)), label='White Noise')
plt.ylim(-0.18, 0.18)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('White Noise Process with TR Volatility')
plt.grid(True)
plt.show()