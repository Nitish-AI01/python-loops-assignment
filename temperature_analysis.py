import numpy as np
import time
# ==========================================
# TASK 1: Temperature Data Processing
# ==========================================

# Create Celsius array
temps_celsius = np.array([22, 25, 28, 24, 26])

# Convert to Fahrenheit (no loops)
temps_fahrenheit = temps_celsius * 1.8 + 32

# Calculate average Fahrenheit (rounded to 1 decimal place)
avg_fahrenheit = round(np.mean(temps_fahrenheit), 1)

print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", avg_fahrenheit)
print()
# ==========================================
# TASK 2: Array Shape and Statistics
# ==========================================

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

# Shape
print("Shape:", scores.shape)

# Total elements
print("Total elements:", scores.size)

# Highest and lowest
highest = np.max(scores)
lowest = np.min(scores)

print("Highest score:", highest)
print("Lowest score:", lowest)

# Range
print("Range:", highest - lowest)
print()
# ==========================================
# TASK 3: Performance Comparison
# ==========================================

# Create data
np_array = np.arange(1, 50001)
py_list = list(range(1, 50001))

# NumPy timing
start_np = time.time()
np_sum = np.sum(np_array)
end_np = time.time()
np_time = round(end_np - start_np, 4)

# Python timing
start_py = time.time()
py_sum = sum(py_list)
end_py = time.time()
py_time = round(end_py - start_py, 4)

# Speed comparison
speed = round(py_time / np_time, 1) if np_time != 0 else "Very fast"

print("NumPy sum:", np_sum)
print("Python sum:", py_sum)
print("NumPy time:", np_time, "seconds")
print("Python time:", py_time, "seconds")

if isinstance(speed, float):
    print(f"NumPy is {speed}x faster")
else:
    print("NumPy is significantly faster")
