import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values (excluding x = 0 to avoid division by zero)
x = np.linspace(-10, 10, 400)
x = x[x != 0]

# Calculate the corresponding y values using the function y = sin(x) / (3x)
y = np.sin(x) / (3*x)

# Create the plot
plt.plot(x, y, label='$y = \\frac{\\sin(x)}{3x}$')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = \\frac{\\sin(x)}{3x}$')

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()