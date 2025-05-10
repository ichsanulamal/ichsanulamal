## 1. Introduction

### Introduction to Matrices, Linear Algebra, and Vectors

In this unit, we're going to explore some of the most powerful tools used in building self-driving cars: matrices, linear algebra, and vectors. These concepts might seem a bit daunting at first, but they're actually very intuitive once you get the hang of them. Many students find these topics challenging, but don't worry—this introduction is designed to make everything clear and understandable. If you're already familiar with these topics, you might breeze through the material. However, if these concepts are new to you, this unit will help demystify the complex ideas often encountered when learning about advanced topics like Kalman filters.

### Welcome to the World of Kalman Filters

Now, let's dive into the fascinating world of Kalman filters by taking a virtual trip to Stanford University, where much of the pioneering work in self-driving technology began.

Behind me is Vale, Stanford's Research Center, where many groundbreaking projects in autonomous vehicles have been developed. One of the most notable achievements is Junior, Stanford's latest self-driving car, which builds on the legacy of Stanley—another autonomous vehicle that is now a part of the National Museum of American History in Washington, D.C.

#### The Equipment Behind Self-Driving Cars

Junior is equipped with several key technologies that make it possible for the car to drive itself. Let's break down some of the essential components:

1. **Laser Range Finder (LIDAR)**:
   - This rotating device is crucial for self-driving functionality. It scans the surroundings 10 times per second, gathering about a million data points each time. The data collected helps the car detect other vehicles and obstacles, preventing collisions. This is where the Kalman filter comes into play, as it processes the data from the LIDAR to make sense of the environment.

2. **Cameras**:
   - On top of the car, there's a camera system, including stereo cameras that capture images from different angles. These cameras provide the car with visual information about its surroundings, aiding in tasks like object detection and lane following.

3. **GPS Antennas**:
   - At the rear of the car, GPS antennas help determine the car's position in the world. This system is crucial for localization, which is the process of figuring out the car's exact location relative to a map. The GPS data complements the data from the LIDAR and cameras.

#### How the Data Feeds into the Kalman Filter

The image you see is a representation of the data coming from the LIDAR. The car is currently parked in a garage, and the image shows the range measurements—distances to nearby objects, such as the back wall of the garage. These measurements are essential inputs to the Kalman filter.

### What is a Kalman Filter?

A Kalman filter is an algorithm that takes noisy sensor data (like the range measurements from the LIDAR) and combines it with a mathematical model of the system (in this case, the car's movement) to estimate the true state of the system. For example, it helps the car understand exactly where it is, how fast it's moving, and where obstacles are, even when the sensor data is imperfect.

### Why Matrices, Linear Algebra, and Vectors?

The core of the Kalman filter and many other algorithms in self-driving cars lies in matrices, linear algebra, and vectors. These tools allow us to represent and manipulate the data in a structured way, making it possible to perform the complex calculations needed for real-time decision-making in autonomous vehicles.

In this unit, you'll learn how to use these mathematical tools to understand and implement algorithms like the Kalman filter. By the end, you'll have a solid foundation in these concepts and a deeper understanding of how they apply to the exciting world of self-driving cars. Let's get started!

## 2. Tracking Introduction

### Journey into Self-Driving Car Technology at Stanford

Welcome to this exciting journey into the world of self-driving cars at Stanford University! Today, we'll be taking a close look at how these cars use sensors to perceive their environment. Let's dive right into our class.

### Recap: Localization in Autonomous Systems

In our last class, we explored the concept of **localization**, where a robot or a self-driving car uses its sensors to determine its position within an environment. This process is crucial for navigating accurately. For instance, the Google self-driving car you see here uses a roadmap to localize itself, understanding exactly where it is in the world.

### Beyond Localization: Tracking Other Vehicles

But localization is just one piece of the puzzle. Today, we’re going to focus on another critical aspect of self-driving technology: **tracking other vehicles**. This capability is vital because, in addition to knowing where our car is, we need to be aware of the location and movement of other vehicles on the road. Why? Because we definitely don't want to collide with them!

Here’s how it works: The self-driving car is equipped with sensors like **lasers** and **radars** that detect other vehicles. The data from these sensors helps the car to not only locate other vehicles but also estimate their speed and direction. This allows the car to make safe driving decisions, avoiding potential accidents.

### The Importance of Tracking for Safety

Tracking isn’t just about cars. It's also crucial for identifying pedestrians and cyclists. Understanding where these entities are and predicting their movements is essential for the safe operation of self-driving vehicles. This ability to foresee where other objects will move in the future ensures that the car can take appropriate actions to avoid collisions.

### Introducing the Kalman Filter: A Key Tracking Technique

To achieve this, we use a technique known as the **Kalman Filter**. This is an incredibly popular method for estimating the state of a dynamic system—in this case, the positions and velocities of other cars or objects.

The Kalman Filter is somewhat similar to the **Monte Carlo localization** technique we discussed in our previous class. However, there are some key differences:

- **Continuous State Estimation**: The Kalman Filter estimates the state in a continuous manner, allowing for smooth predictions. In contrast, Monte Carlo localization works by dividing the world into discrete segments, which can limit its resolution.
  
- **Uni-modal Distribution**: The Kalman Filter provides us with a uni-modal distribution, meaning it predicts a single most likely state. Monte Carlo localization, on the other hand, can handle multiple possible states (multi-modal distributions).

### Applying the Kalman Filter to Vehicle Tracking

Let’s consider a simple scenario to understand how the Kalman Filter works in practice:

Imagine our self-driving car detects another vehicle at four different time points: at \( t = 0 \), \( t = 1 \), \( t = 2 \), and \( t = 3 \). Each of these measurements gives us the position of the vehicle at that specific time.

Now, based on these observations, where would you expect the vehicle to be at \( t = 4 \)?

#### Predicting the Next Position

The Kalman Filter helps us answer this question. By analyzing the pattern of the vehicle's movement, it can predict where the vehicle will be at the next time step. This prediction is based on the assumption that the vehicle's movement follows a certain pattern, such as constant speed or acceleration.

The Kalman Filter continuously updates its predictions as new sensor data comes in, making it a powerful tool for real-time tracking in self-driving cars.

### Conclusion

In this class, we've begun to explore the critical concept of tracking in autonomous vehicles. The Kalman Filter is a key technique that enables these vehicles to not only understand where other objects are but also to predict where they will be in the future. This ability is essential for ensuring the safety of everyone on the road, from other drivers to pedestrians and cyclists.

Next, we'll dive deeper into the mathematics and algorithms behind the Kalman Filter, breaking down how it works step by step. Get ready to explore the powerful world of predictive tracking!

## 3. KALMAN Gaussian Introduction

### Background: Histograms vs. Gaussians

1. **Histograms**:
   - A histogram is a way to approximate a probability distribution.
   - It divides a continuous space into discrete grid cells.
   - Each grid cell gets assigned a probability.
   - It's a simple approximation of the underlying continuous distribution.

2. **Gaussian Distributions (Normal Distributions)**:
   - Unlike histograms, Gaussians represent continuous probability distributions.
   - They are characterized by two key parameters:
     - **Mean (μ)**: The center of the distribution.
     - **Variance (σ²)**: The spread or "width" of the distribution.
   - A Gaussian function is smooth and continuous, and the total area under the curve equals 1.

### Gaussian Function in 1D

The 1D Gaussian function is defined as:

\[
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
\]

Where:
- \( x \) is the variable.
- \( \mu \) is the mean.
- \( \sigma^2 \) is the variance.
- The term \(\exp\) denotes the exponential function.

#### Key Points:
- **Exponential of a Quadratic**: The Gaussian function involves an exponential term where the exponent is a negative quadratic function of \(x\).
- **Normalization Constant**: \( \frac{1}{\sqrt{2\pi\sigma^2}} \) ensures that the area under the curve sums to 1, making it a valid probability distribution.
  - For many applications, this constant can be ignored because it doesn't affect the shape of the Gaussian, only the scaling.

### Practical Example
To visualize a Gaussian:

1. **When \(x = \mu\)**: The exponential term becomes \(\exp(0) = 1\), meaning the Gaussian reaches its peak.
2. **As \(x\) moves away from \(\mu\)**: The exponential term decreases, leading to lower values of \(f(x)\).

### Key Concept: Gaussian as an Approximation

- In Kalman Filters and similar techniques, instead of estimating the whole distribution using a histogram, we approximate it using a Gaussian characterized by \( \mu \) and \( \sigma^2 \). This is computationally efficient and works well in practice for many problems.

### Visualization: Identifying a Gaussian

To recognize a Gaussian curve, look for:
- A symmetric bell-shaped curve.
- The peak is at \( \mu \).
- The curve tails off smoothly as you move away from \( \mu \) in both directions.

## 4. Maximize Gaussian

Let's break down the steps and find the solution.

### Gaussian Function Recap

The Gaussian function in 1D is given by:

\[
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
\]

Given parameters:
- \( \mu = 10 \)
- \( \sigma^2 = 4 \)
- \( x = 8 \)

### Step 1: Constant Calculation

The constant part is:

\[
\text{constant} = \frac{1}{\sqrt{2\pi\sigma^2}} = \frac{1}{\sqrt{2\pi \times 4}}
\]

### Step 2: Exponential Part Calculation

The exponential part is:

\[
\text{exponential} = \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right) = \exp\left(-\frac{(8 - 10)^2}{2 \times 4}\right)
\]

### Step 3: Function Calculation

Now, combining these two parts:

\[
f(8) = \frac{1}{\sqrt{8\pi}} \exp\left(-\frac{(-2)^2}{8}\right) = \frac{1}{\sqrt{8\pi}} \exp\left(-\frac{4}{8}\right)
\]

You mentioned the output should be approximately 0.12, so this should match with our calculations.

### Step 4: Finding the Maximum Value

To maximize the function \( f(x) \), we need to maximize the exponential part, which occurs when the exponent is zero. 

\[
-\frac{(x - \mu)^2}{2\sigma^2} = 0
\]

This happens when:

\[
x = \mu
\]

So, to maximize \( f(x) \), you should set \( x \) equal to \( \mu = 10 \).

### Final Answer

To get the maximum value of the Gaussian function, you should modify \( x = 8 \) to \( x = 10 \). The function \( f(10) \) will be at its peak, giving you the maximum return value for this function.

## Quiz

Let's break down and explain the concepts related to Kalman Filters and Gaussian updates from the quizzes.

### 1. **Measurement Update and Prediction Update**:
   - **Measurement Update**: This step involves incorporating new information from a measurement into the prior belief (which is often represented as a Gaussian distribution). In Kalman Filters, the measurement update uses Bayes' Rule to combine the prior distribution with the measurement distribution, resulting in a posterior distribution. The posterior's mean is typically shifted towards the mean of the measurement, and its variance is adjusted based on the measurement's certainty.
   - **Prediction Update**: This step projects the current belief about the state forward in time, based on some motion model or dynamics of the system. It typically increases the uncertainty (variance) because we are less certain about where the state might be after the motion.

### 2. **Shifting the Mean**:
   - When you receive a new measurement, the mean of the resulting posterior Gaussian is a weighted average of the prior mean and the measurement mean. The weights are determined by the variances (uncertainties) of each distribution. If the measurement is more certain (smaller variance), the new mean will be closer to the measurement mean.

   - **Quiz Answer Explanation**: The new mean lies between the prior mean and the measurement mean, closer to the measurement mean if the measurement is more certain.

### 3. **Predicting the Peak**:
   - When two Gaussians are multiplied (as in the measurement update), the result is a new Gaussian distribution with a mean somewhere between the means of the original Gaussians, and a variance that is smaller than either of the original variances. This reduction in variance reflects the fact that you have gained information by combining two sources of data.
  
   - **Quiz Answer Explanation**: The correct posterior Gaussian is the one that is narrower and has a peak in between the two original Gaussians, indicating increased certainty about the estimated state.

### 4. **Parameter Update**:
   - **New Mean (\(\mu'\))**: The new mean after the measurement update is given by a weighted sum of the old mean (\(\mu\)) and the measurement mean (\(\nu\)):
     \[
     \mu' = \frac{\sigma^2 \nu + r^2 \mu}{\sigma^2 + r^2}
     \]
   - **New Variance (\(\sigma'^2\))**: The new variance is given by:
     \[
     \sigma'^2 = \frac{\sigma^2 r^2}{\sigma^2 + r^2}
     \]
     This results in a variance smaller than either \(\sigma^2\) or \(r^2\), reflecting increased certainty after incorporating the measurement.

   - **Quiz Answer Explanation**: If the prior and measurement Gaussians have the same variance, the new mean is exactly halfway between the two means, and the new variance is half of the original variance, as the two uncertainties have been combined into a more certain estimate.

### Summary
- In the Kalman filter, both the mean and variance of the state estimate are updated using a combination of the prior information and new measurements. The new mean is a weighted average that shifts towards the more certain measurement, and the new variance decreases, reflecting increased certainty.
- The key idea is that combining two uncertain estimates can yield a more certain overall estimate, hence a narrower Gaussian distribution in the posterior. 

These concepts form the basis of the Kalman filter, a powerful tool in various applications, including robotics, navigation, and finance.

---

Let's break down the concepts from the excerpts into a more structured format for learning, focusing on the Kalman filter, particularly the measurement and prediction steps.

### 1. **Kalman Filter Overview**
The Kalman filter is a powerful tool used for estimating the state of a system where there is uncertainty in the measurements. It's widely used in robotics, navigation, and financial modeling.

### 2. **Key Components**
   - **State Estimate (Mean, \( \mu \))**: Represents the best guess of the state of the system.
   - **Uncertainty (Variance, \( \sigma^2 \))**: Represents the confidence in the state estimate. A higher variance means more uncertainty.

### 3. **Two Main Steps in Kalman Filter**
   - **Measurement Update (Correction Step)**: Integrates new measurements to update the estimate.
   - **Prediction (Motion Update)**: Projects the current estimate forward based on a known motion model.

### 4. **Measurement Update Step**
   - **New Mean**: The updated mean \( \mu_{\text{new}} \) after incorporating the measurement.
   - **New Variance**: The updated variance \( \sigma_{\text{new}}^2 \) after incorporating the measurement.

   The formulas used:
   - New Mean: 
     \[
     \mu_{\text{new}} = \frac{\sigma_{\text{meas}}^2 \cdot \mu_{\text{prior}} + \sigma_{\text{prior}}^2 \cdot \mu_{\text{meas}}}{\sigma_{\text{prior}}^2 + \sigma_{\text{meas}}^2}
     \]
   - New Variance:
     \[
     \sigma_{\text{new}}^2 = \left(\frac{1}{\sigma_{\text{prior}}^2} + \frac{1}{\sigma_{\text{meas}}^2}\right)^{-1}
     \]

### 5. **Prediction Step**
   - **Updated Mean**: The mean is updated by adding the expected movement \( u \) to the current mean.
   - **Updated Variance**: The variance increases due to the added uncertainty from the motion.

   The formulas used:
   - Predicted Mean:
     \[
     \mu_{\text{pred}} = \mu_{\text{prior}} + u
     \]
   - Predicted Variance:
     \[
     \sigma_{\text{pred}}^2 = \sigma_{\text{prior}}^2 + \sigma_{\text{motion}}^2
     \]

### 6. **Example for Measurement Update**
   - Let's say you have two estimates with means \( \mu_1 = 10 \) and \( \mu_2 = 12 \), both having equal variances \( \sigma_1^2 = \sigma_2^2 = 4 \).
   - Applying the formulas, the new mean will be:
     \[
     \mu_{\text{new}} = \frac{4 \cdot 10 + 4 \cdot 12}{4 + 4} = 11
     \]
   - The new variance:
     \[
     \sigma_{\text{new}}^2 = \left(\frac{1}{4} + \frac{1}{4}\right)^{-1} = 2
     \]

### 7. **Example for Prediction Step**
   - Suppose you have a prior estimate with \( \mu_{\text{prior}} = 10 \) and \( \sigma_{\text{prior}}^2 = 4 \). You move to the right by 10 units with a motion uncertainty \( \sigma_{\text{motion}}^2 = 6 \).
   - The predicted mean:
     \[
     \mu_{\text{pred}} = 10 + 10 = 20
     \]
   - The predicted variance:
     \[
     \sigma_{\text{pred}}^2 = 4 + 6 = 10
     \]

### 8. **Summary**
In summary, the Kalman filter alternates between the measurement update, where it refines its estimate based on new data, and the prediction step, where it projects the estimate forward in time. Understanding these steps and their implementation in code is key to effectively using Kalman filters.

## Code

Sure! Let's break down the task of implementing the Kalman Filter as described and then write the code for it.

### Problem Breakdown:
1. **Initial Setup:**
   - Initial estimate (`mu`) = 0
   - Initial uncertainty (`sig`) = 10,000

2. **Measurements and Motions:**
   - Measurements: [5., 6., 7., 9., 10.]
   - Motions: [1., 1., 2., 1., 1.]

3. **Uncertainties:**
   - Measurement uncertainty (`measurement_sig`) = 4
   - Motion uncertainty (`motion_sig`) = 2

4. **Functions:**
   - `update`: To update the belief based on a new measurement.
   - `predict`: To predict the next state based on motion.

### Mathematical Formulation:

1. **Update (Bayes' rule)**:
   \[
   \mu' = \frac{(\text{sig} \times \text{measurement}) + (\text{measurement\_sig} \times \mu)}{\text{sig} + \text{measurement\_sig}}
   \]
   \[
   \text{sig}' = \left(\frac{1}{\text{sig}} + \frac{1}{\text{measurement\_sig}}\right)^{-1}
   \]

2. **Predict (Motion model)**:
   \[
   \mu'' = \mu' + \text{motion}
   \]
   \[
   \text{sig}'' = \text{sig}' + \text{motion\_sig}
   \]

### Code Implementation:

```python
def update(mu, sig, measurement, measurement_sig):
    new_mu = (sig * measurement + measurement_sig * mu) / (sig + measurement_sig)
    new_sig = 1 / (1 / sig + 1 / measurement_sig)
    return new_mu, new_sig

def predict(mu, sig, motion, motion_sig):
    new_mu = mu + motion
    new_sig = sig + motion_sig
    return new_mu, new_sig

# Initial values
mu = 0
sig = 10000

# Measurements and motions
measurements = [5., 6., 7., 9., 10.]
motions = [1., 1., 2., 1., 1.]

# Uncertainties
measurement_sig = 4
motion_sig = 2

# Process the measurements and motions
for measurement, motion in zip(measurements, motions):
    mu, sig = update(mu, sig, measurement, measurement_sig)
    print(f"Update: mu = {mu}, sig = {sig}")
    mu, sig = predict(mu, sig, motion, motion_sig)
    print(f"Predict: mu = {mu}, sig = {sig}")

# Final estimated position and uncertainty
print(f"Final Estimate: mu = {mu}, sig = {sig}")
```

### Expected Output:
When you run this code, it will give you the following output:

```
Update: mu = 4.998000799680128, sig = 3.9984006397441023
Predict: mu = 5.998000799680128, sig = 5.998400639744102
Update: mu = 5.999200191953932, sig = 2.399744061425258
Predict: mu = 6.999200191953932, sig = 4.399744061425258
Update: mu = 6.999619127420922, sig = 2.0951800575117594
Predict: mu = 8.999619127420922, sig = 4.09518005751176
Update: mu = 8.999811802788143, sig = 2.0235152416216957
Predict: mu = 9.999811802788143, sig = 4.023515241621696
Update: mu = 9.999905433919556, sig = 2.0058615808441944
Predict: mu = 10.999905433919556, sig = 4.005861580844194
Final Estimate: mu = 10.999905433919556, sig = 4.005861580844194
```

This code implements the Kalman Filter in Python, and the output should match the expected final result mentioned in your example.

---

Your detailed explanation highlights how the Kalman filter balances between initial beliefs and incoming measurements. Let's break it down further and analyze what happens when the initial certainty (or uncertainty) changes:

### Key Concepts:
1. **Initial Estimate (`mu`) and Uncertainty (`sig`):**
   - These define your prior belief about the system's state.
   - If your initial uncertainty is low (meaning you are confident in your initial estimate), the Kalman filter will be less responsive to new measurements.
   - Conversely, if your initial uncertainty is high, the Kalman filter will rely more on the incoming measurements.

2. **Measurement and Motion Updates:**
   - **Measurement Update:** Adjusts the current state estimate (`mu`) based on a new measurement. The more certain the measurement (lower `measurement_sig`), the more influence it has on the updated estimate.
   - **Motion Update:** Adjusts the current state estimate based on the applied motion. The motion uncertainty (`motion_sig`) affects how much confidence you have in the prediction after motion is applied.

### Experimenting with Different Initial Uncertainty Values:

1. **High Initial Uncertainty (e.g., `sig = 10000`):**
   - The filter quickly shifts towards the first measurement since the initial belief is weak.
   - As you saw, after the first measurement, the position estimate (`mu`) quickly approaches the true value.

2. **Low Initial Uncertainty (e.g., `sig = 1` or smaller):**
   - The filter is more "stubborn" and sticks closely to the initial estimate even if it's wrong.
   - It takes several measurements to "drag" the estimate towards the true value, and the final estimate may not fully correct the initial mistake.

### Example Code for Testing Different Initial Uncertainties:

```python
def update(mu, sig, measurement, measurement_sig):
    new_mu = (sig * measurement + measurement_sig * mu) / (sig + measurement_sig)
    new_sig = 1 / (1 / sig + 1 / measurement_sig)
    return new_mu, new_sig

def predict(mu, sig, motion, motion_sig):
    new_mu = mu + motion
    new_sig = sig + motion_sig
    return new_mu, new_sig

# Experiment 1: High initial uncertainty
mu = 0
sig = 10000  # High initial uncertainty

# Measurements and motions
measurements = [5., 6., 7., 9., 10.]
motions = [1., 1., 2., 1., 1.]

# Uncertainties
measurement_sig = 4
motion_sig = 2

print("High Initial Uncertainty:")
for measurement, motion in zip(measurements, motions):
    mu, sig = update(mu, sig, measurement, measurement_sig)
    print(f"Update: mu = {mu}, sig = {sig}")
    mu, sig = predict(mu, sig, motion, motion_sig)
    print(f"Predict: mu = {mu}, sig = {sig}")
print(f"Final Estimate: mu = {mu}, sig = {sig}\n")

# Experiment 2: Low initial uncertainty
mu = 0
sig = 1  # Low initial uncertainty

print("Low Initial Uncertainty:")
for measurement, motion in zip(measurements, motions):
    mu, sig = update(mu, sig, measurement, measurement_sig)
    print(f"Update: mu = {mu}, sig = {sig}")
    mu, sig = predict(mu, sig, motion, motion_sig)
    print(f"Predict: mu = {mu}, sig = {sig}")
print(f"Final Estimate: mu = {mu}, sig = {sig}")
```

### Expected Results:

- **High Initial Uncertainty:**
  - The estimate (`mu`) quickly aligns with the measurements, and the uncertainty (`sig`) decreases significantly after the first few updates.
  
- **Low Initial Uncertainty:**
  - The estimate (`mu`) moves slowly towards the true value, and even after all updates, the final estimate may still be biased by the initial wrong estimate.

### Conclusion:
The Kalman filter effectively "learns" the true state by balancing the initial estimate with new data. The initial uncertainty plays a critical role in how quickly the filter adapts to new measurements. By adjusting this uncertainty, you can see how the filter’s behavior changes, which is key in understanding the underlying mechanics of this algorithm.

## Summary

### Understanding the Kalman Filter in 2D Spaces

You've got a good handle on the 1D Kalman Filter, which is excellent. Now, let's extend this understanding to a 2D scenario. This is where things get more interesting and practical, especially for real-world applications like tracking objects with sensors.

#### 1D vs. 2D Kalman Filter

- **1D Kalman Filter:** In a 1D scenario, the Kalman Filter helps you estimate the position of an object along a single axis (like the x-axis). You incorporate measurements (sensor readings) and motions (movements) to predict the object's future location.

- **2D Kalman Filter:** When you move to a 2D state space, you track the object in two dimensions, like x and y (imagine a camera image or radar system tracking a vehicle on a plane). The Kalman Filter now estimates the position in both x and y, as well as inferring the object's velocity in each direction, even if the sensor only directly measures position.

#### Example: Tracking an Object in 2D

Suppose you're tracking a car using radar. At time \( t = 0 \), the car is at a specific coordinate \((x_0, y_0)\). After one time-step, the car moves to \((x_1, y_1)\), and after another time-step, it moves to \((x_2, y_2)\). 

Now, you want to predict where the car will be at time \( t = 3 \).

- **Without Kalman Filter:** You might simply guess based on the last position, which could lead to inaccuracies.
  
- **With Kalman Filter:** The filter not only uses the positions \((x_0, y_0)\), \((x_1, y_1)\), and \((x_2, y_2)\) but also infers the car's velocity (how fast it's moving in the x and y directions). This allows the Kalman Filter to make a much more accurate prediction about where the car will be at \( t = 3 \).

#### Key Insight

The sensor doesn't directly measure velocity; it only gives you positions at different times. However, the Kalman Filter is powerful enough to infer the velocity from these positions and then use this inferred velocity to predict future positions. This capability is why Kalman Filters are widely used in AI and control theory for tracking and prediction tasks.

### Why Kalman Filters are Popular

Kalman Filters are popular because of their ability to estimate variables (like velocity) that are not directly measured but are crucial for making accurate predictions. In higher-dimensional spaces, this ability becomes even more powerful, enabling the tracking of complex systems with multiple state variables.