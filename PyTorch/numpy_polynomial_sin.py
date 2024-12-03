# -*- coding: utf-8 -*-
import numpy as np
import math

# Create random input and output data
x = np.linspace(-math.pi, math.pi, 2000)
y = np.sin(x)

# Randomly initialize weights
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y
    # y = a + b x + c x^2 + d x^3
    y_pred = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    # The loss measures the difference between the predicted values (y_pred) and the actual values (x)
    loss = np.square(y_pred - y).sum()
    if t % 100 == 99:
        print(t, loss)


    # Backprop to compute gradients of a, b, c, d with respect to loss
    # gradient is the derivative of the loss with respect to each parameter

    grad_y_pred = 2.0 * (y_pred - y)
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights
    # Gradient Descent Update
    # The weights are updated using the gradients and the learning_rate
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')
# final function will approximate sin(x) reasonably well near the origin (small values of 𝑥)
# but diverges significantly for larger ∣𝑥∣
# This behavior is typical for low-order polynomial approximations:
# they are accurate within a limited range but fail to capture the periodic nature of trigonometric functions like
# sin(x)