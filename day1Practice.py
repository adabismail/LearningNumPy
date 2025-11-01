import numpy as np

#Q1
even_arr = np.arange(10, 40, 2)

print(f"Array: {even_arr}")
print(f"Number of elements in the array: {even_arr.size}")

reshaped_arr = even_arr.reshape(3,5)
print(f"Reshaped array: \n{reshaped_arr}")
print(f"Shape of the final array: {reshaped_arr.shape}")

print("\n")

#Q2
constant_matrix = np.full((4,4), 10.5)
print(constant_matrix)
print(f"Size of const matrix: {constant_matrix.size}")
print(f"dimensions of const matrix: {constant_matrix.ndim}")


print("\n")


#Q3
random_arr = np.random.randint(1,21, (3,3))
print(random_arr)
ravaled_view = random_arr.ravel()
flatened_view = random_arr.flatten()

ravaled_view[0] = 999
flatened_view[0] = 111

print(random_arr)


print("\n"*3)


#Q4
rand_f_matrix = np.random.random((2,5))
print(f"Og matrix: {rand_f_matrix} and shape: {rand_f_matrix.shape}")
transposed_matrix = rand_f_matrix.T
print(f"Transposed matrix: {transposed_matrix}, and shape: {transposed_matrix.shape}")

print("\n"*10)
#Q5

final_array = np.arange(0,24)
reshaped_final_arr = final_array.reshape(2,3,4)
print(f"Final array: {final_array}")
print(f"Reshaped array: {reshaped_final_arr}\n with size: {reshaped_final_arr.size}, shape: {reshaped_final_arr.shape}, and dimension: {reshaped_final_arr.ndim}")

print(reshaped_final_arr[0][2][2])


#NumPy Challenge: Set 2
# Question 1: The Strided Matrix
# Create a 1D NumPy array containing all integers from 0 to 63 (inclusive).
# Reshape this array into an 8x8 matrix.
# From this 8x8 matrix, create a new 4x4 matrix that contains only the elements where both the row index and the column index are even. (e.g., the elements from [0, 0], [0, 2], [0, 4], [0, 6], [2, 0], [2, 2], etc.).
# Print the final 4x4 matrix.

# Question 2: The "Center-Out" Transpose
# Create a 5x5 matrix of random integers, with values between 10 and 99.
# Print the original 5x5 matrix.
# Extract the inner 3x3 "core" of this matrix (i.e., everything except the first and last rows and columns).
# Create a transposed version of this 3x3 core.
# Replace the original 3x3 core inside the 5x5 matrix with its transposed version.
# Print the final, modified 5x5 matrix.

# Question 3: The View vs. Copy Puzzle
# Create a 1D array of integers from 1 to 12 (inclusive).
# Create a 3x4 matrix named mat_a by reshaping the original array.
# Create a 1D array named flat_b by calling mat_a.flatten().
# Create a 1D array named rav_c by calling mat_a.ravel().
# Set the last element (index -1) of flat_b to 111.
# Set the first element (index 0) of rav_c to 999.
# Now, print the original matrix, mat_a.

# Question 4: The 3D Block Assignment
# Create a 3D array with the shape (4, 2, 3) and fill it with all zeros.
# Modify this 3D array in place by setting all the values in the first "page" (i.e., at index 0) to the number 5.
# Modify the array again by setting all the values in the last "page" (i.e., at index 3) to the number 9.
# Print the final 3D array.

# Question 5: The Checkerboard Challenge
# Create an 8x8 matrix filled with all zeros, ensuring its dtype is int.
# Modify this 8x8 matrix in place so that it becomes a checkerboard pattern of 0s and 1s. The element at [0, 0] (top-left) should be 1.
# Print the final 8x8 checkerboard matrix.