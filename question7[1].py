import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(-10, 10, 400)

# Calculate the corresponding y values using the function y = x^3 + 2x^2 - 10x + 3
y = x**3 + 2*x**2 - 10*x + 3

# Create the plot
plt.plot(x, y, label='$y = x^3 + 2x^2 - 10x + 3$')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^3 + 2x^2 - 10x + 3$')

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()