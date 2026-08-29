import math

def f(x):
    return math.exp((x - 1)**2) - 1


def secant_method(x_prev, x, tolerance=1e-6, max_iterations=100):

    for i in range(1, max_iterations + 1):

        x_new = x - f(x) * (x - x_prev) / (f(x) - f(x_prev))

        print(f"Iteration {i}: x = {x_new:.10f}")

        if abs(x_new - x) < tolerance:
            return x_new, i

        x_prev = x
        x = x_new

    return x, max_iterations


def modified_secant_method(x_prev, x, m=2,
                           tolerance=1e-6,
                           max_iterations=100):

    for i in range(1, max_iterations + 1):

        x_new = x - m * f(x) * (x - x_prev) / (f(x) - f(x_prev))

        print(f"Iteration {i}: x = {x_new:.10f}")

        if abs(x_new - x) < tolerance:
            return x_new, i

        x_prev = x
        x = x_new

    return x, max_iterations



x_minus1 = -0.5
x0 = 0.0

tolerance = 1e-6


print("======================================")
print("       STANDARD SECANT METHOD")
print("======================================")

root_secant, iterations_secant = secant_method(
    x_minus1,
    x0,
    tolerance
)

print("\nRoot =", root_secant)
print("Number of iterations =", iterations_secant)


print("\n======================================")
print("       MODIFIED SECANT METHOD")
print("======================================")

root_modified, iterations_modified = modified_secant_method(
    x_minus1,
    x0,
    m=2,
    tolerance=tolerance
)

print("\nRoot =", root_modified)
print("Number of iterations =", iterations_modified)



print("\n======================================")
print("             COMPARISON")
print("======================================")

print("Secant Method iterations =", iterations_secant)
print("Modified Secant iterations =", iterations_modified)

print("\nBoth methods converge to the root x = 1.")