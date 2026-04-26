import time
import numpy as np

q = 17

A = np.array([[1, 2, 3, 1],
              [2, 1, 1, 2],
              [3, 1, 2, 1],
              [1, 3, 1, 2]])

s = np.array([1, -1, 0, 1])

def matrix_operation():
    return (A @ s) % q

def polynomial_multiply(a, b):
    return np.convolve(a, b)

def average_time(function, runs=5000):
    start = time.perf_counter()
    for _ in range(runs):
        function()
    end = time.perf_counter()
    return (end - start) / runs

a = np.array([1, 2, 1, 0])
b = np.array([2, 1, 0, 1])

matrix_time = average_time(matrix_operation)
poly_time = average_time(lambda: polynomial_multiply(a, b))

print("Week 11 - Operation Timing")
print("--------------------------")
print("Matrix result:", matrix_operation())
print("Average matrix time:", matrix_time * 1_000_000, "microseconds")
print("Average polynomial time:", poly_time * 1_000_000, "microseconds")
print("q =", q)
print("These are small toy operations.")
