# Let's correct the approach for calculating and plotting the decision boundary based on given coefficients and data.

import numpy as np
import matplotlib.pyplot as plt

# Given data for omega_1 and omega_2
omega_1 = np.array([[1, 2], [3, 1], [5, 2], [3, 3]]).T  # Transpose to match provided code's structure
omega_2 = np.array([[6, 6], [8, 5], [10, 6], [8, 7]]).T

# Calculated means
omega1_mean = np.mean(omega_1, axis=1)
omega2_mean = np.mean(omega_2, axis=1)

# Combined covariance and its inverse
omega1_var = np.cov(omega_1)
omega2_var = np.cov(omega_2)
inv_Sigma = np.linalg.inv((omega1_var + omega2_var) / 2)

# Coefficients for linear decision boundary
coef_1 = inv_Sigma @ (omega1_mean - omega2_mean)
coef_2 = -0.5 * (omega1_mean.T @ inv_Sigma @ omega1_mean) + 0.5 * (omega2_mean.T @ inv_Sigma @ omega2_mean) + np.log(0.5 / 0.5)

# Plotting data points
plt.scatter(omega_1[0], omega_1[1], color='red', label='Class 1')
plt.scatter(omega_2[0], omega_2[1], color='blue', label='Class 2')

# Generating points for decision boundary
x = np.linspace(0, 10, 100)
y = (-coef_1[0] * x - coef_2) / coef_1[1]
plt.plot(x, y, label='Decision Boundary', color='green')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Data Points and Decision Boundary')
plt.grid(True)
plt.show()
