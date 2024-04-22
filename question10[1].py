import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (x + 2) * (x + 3) * (x - 4)

# Generate x values
x = np.linspace(-5, 5, 400)

# Generate y values
y = f(x)

# Plot the function
plt.plot(x, y)
plt.title('Plot of f(x) = (x + 2)(x + 3)(x - 4)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()