import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values (excluding x = 0 to avoid division by zero)
x = np.linspace(-10, 10, 400)
x = x[x != 0]

# Calculate the corresponding y values using the function y = (x^3 / (2x)) - 10x
y = (x**3 / (2*x)) - 10*x

# Create the plot
plt.plot(x, y, label='$y = \\frac{x^3}{2x} - 10x$')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = \\frac{x^3}{2x} - 10x$')

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()