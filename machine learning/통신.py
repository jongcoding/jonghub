import numpy as np
import matplotlib.pyplot as plt

# Constants
n_values = np.arange(-11, 12, 1)
T0 = 2 * np.pi
omega0 = 1

# Compute Dn
D_n = np.sin(n_values * np.pi / 2) / (n_values * np.pi)
D_n[n_values == 0] = 1 / T0  # Correcting the value when n = 0 (avoid division by zero)

# Compute C0 and Cn
C_0 = D_n[n_values == 0]
C_n = 2 * np.abs(D_n[n_values != 0])

# Calculate power up to n=7
power_indices = np.arange(-7, 8, 1)
power = np.sum(np.abs(D_n[np.isin(n_values, power_indices)])**2)

# Plotting |D_n| and C_n
fig, ax = plt.subplots(2, 1, figsize=(10, 10))
# Plot for |D_n|
ax[0].stem(n_values, np.abs(D_n), use_line_collection=True)
ax[0].set_title("|D_n| vs n")
ax[0].set_xlabel("n")
ax[0].set_ylabel("|D_n|")
ax[0].grid(True)

# Plot for C_n (for n >= 1)
ax[1].stem(n_values[n_values != 0], C_n, use_line_collection=True)
ax[1].set_title("C_n vs n (n >= 1)")
ax[1].set_xlabel("n")
ax[1].set_ylabel("C_n")
ax[1].grid(True)

plt.tight_layout()
plt.show()

print(C_0, power)
