import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(-2, 2, 100)

# Calculate the corresponding y values using the function y = x^4 + x^3 + x^2 + x + 1
y = x**4 + x**3 + x**2 + x + 1

# Create the plot
plt.plot(x, y, label='$y = x^4 + x^3 + x^2 + x + 1$')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^4 + x^3 + x^2 + x + 1$')

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()