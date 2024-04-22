import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(-10, 10, 100)

# Calculate the corresponding y values using the function y = x^2 - 10
y = x**2 - 10

# Create the plot
plt.plot(x, y, label='$y = x^2 - 10$')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^2 - 10$')

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()


