import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp((x - 1)**2) - 1



def fp(x):
    return 2 * (x - 1) * np.exp((x - 1)**2)



def fpp(x):
    return (2 + 4 * (x - 1)**2) * np.exp((x - 1)**2)



x = np.linspace(-1, 3, 1000)


# Plot f(x)
plt.figure()
plt.plot(x, f(x))
plt.axhline(0)
plt.axvline(1)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x)")
plt.grid()
plt.show()



plt.figure()
plt.plot(x, fp(x))
plt.axhline(0)
plt.axvline(1)
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.title("Plot of f'(x)")
plt.grid()
plt.show()



plt.figure()
plt.plot(x, fpp(x))
plt.axhline(0)
plt.axvline(1)
plt.xlabel("x")
plt.ylabel("f''(x)")
plt.title("Plot of f''(x)")
plt.grid()
plt.show()



print("f(1)  =", f(1))
print("f'(1) =", fp(1))
print("f''(1) =", fpp(1))

print("\nSince f(1) = 0, f'(1) = 0 but f''(1) != 0,")
print("the multiplicity of the root x = 1 is 2.")
