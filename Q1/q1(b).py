import numpy as np
import matplotlib.pyplot as plt


# Function f(x)
def f(x):
    return np.exp((x - 1)**2) - 1


# First derivative f'(x)
def fp(x):
    return 2 * (x - 1) * np.exp((x - 1)**2)


# u(x) = f(x) / f'(x)
def u(x):
    t = x - 1

    if abs(t) < 1e-10:
        return 0.0

    return (1 - np.exp(-t**2)) / (2 * t)


# Derivative of u(x)
def up(x):
    t = x - 1

    if abs(t) < 1e-10:
        return 0.5

    return ((2 * t**2 + 1) * np.exp(-t**2) - 1) / (2 * t**2)


# Values of x
x = np.linspace(-1, 3, 1000)

# Remove x = 1 to avoid division by zero in the formula
x_plot = x[np.abs(x - 1) > 1e-10]


# Plot u(x)
u_values = [u(i) for i in x_plot]

plt.figure()
plt.plot(x_plot, u_values)
plt.axhline(0)
plt.axvline(1)
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("Plot of u(x) = f(x)/f'(x)")
plt.grid()
plt.show()


# Plot u'(x)
up_values = [up(i) for i in x_plot]

plt.figure()
plt.plot(x_plot, up_values)
plt.axhline(0)
plt.axvline(1)
plt.xlabel("x")
plt.ylabel("u'(x)")
plt.title("Plot of u'(x)")
plt.grid()
plt.show()


# Check values at x = 1
print("u(1)  =", u(1))
print("u'(1) =", up(1))

print("\nSince u(1) = 0 but u'(1) != 0,")
print("the multiplicity of the root x = 1 is 1.")