import numpy as np


# data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])
# Question 1: The Sales Growth Calculator
# Isolate the sales data for 2024 and 2021 into two separate 1D arrays.
# Calculate the absolute sales growth for each restaurant between 2021 and 2024 (i.e., 2024_sales - 2021_sales).
# Print the resulting 1D array, which should contain the growth amount for each of the 5 restaurants.

sales_2021 = sales_data[:,1]
sales_2024 = sales_data[:,4]
print(f"sales 2021: {sales_2021} \nsales 2024: {sales_2024}")
sales_growth = sales_2024 - sales_2021
print(f"Absolute sales growth: {sales_growth}")
print("\n"*15)
# Question 2: The Correction Factor (Broadcasting)
# Create a 1D array representing a "correction factor" for each year: correction = np.array([1.0, 1.05, 0.95, 1.1])
# Slice the sales_data to get only the sales numbers (a 5x4 matrix).
# Use broadcasting to multiply the entire 5x4 sales matrix by the 1D correction array. This should apply the first factor to the first column (2021), the second to the second column (2022), etc.
# Print the resulting 5x4 "corrected sales" matrix.

sales_number = sales_data[:, 1:]
print(f"Sales Number: \n{sales_number}")
correction = np.array([1.0, 1.05, 0.95, 1.1])
print(f"Correction: \n {correction}")

print(sales_number[:, 0])




print("\n"*15)

# Question 4: The Weighted Restaurant Score (Dot Product)
# Create a 1D array of "year weights": weights = np.array([0.1, 0.2, 0.3, 0.4]). (This gives more weight to recent years).
# Slice the sales_data to get the 5x4 sales matrix.
# Use np.dot() to calculate a final "weighted score" for each of the 5 restaurants. This will be a matrix-vector multiplication.
#  Print the resulting 1D array (shape (5,)), which contains the final score for each restaurant.
weights = np.array([0.1, 0.2, 0.3, 0.4])
sales_data = sales_data[:,1:]
matrix_mult = np.dot(sales_data, weights)
print(matrix_mult)




# Question 5: Deviation From Mean (Broadcasting & Axis)
# Create the 5x4 sales-only matrix from sales_data.
# Calculate the average sales for each restaurant across all four years (i.e., the mean of each row). This will result in a 1D array of shape (5,).
# Using this 1D mean array, use broadcasting to subtract each restaurant's average from its own sales data for all four years. (This will show how much each year's sales deviated from that restaurant's personal average).
# Print the resulting 5x4 "deviation" matrix.


sales_data = sales_data[:,1:]
print(sales_data)
mean_sale = np.mean(sales_data, axis=1, dtype=int)


print(mean_sale)

# deviated = sales_data - mean_sale
# print(deviated)