import numpy as np

# Question 1: The Conditional Row Selector
# Create a 6x4 matrix of random integers with values between 1 and 50.
# Find all the rows where the value in the third column (index 2) is even.
# Select and print only these complete rows.

matrix = np.random.randint(1,51, (6,4))
print(f"Matrix of (6,4):\n {matrix} \n")
# even_matrix = matrix % 2 == 0
# print(even_matrix)

# for i in range(6):
#     if (matrix[i][2]%2) == 0:
#         print(f"Row where index 2 is even : {matrix[i]}")

condition = np.where(matrix[:,2]%2==0) 
print(matrix[condition])       

print("\n"*15)








# Question 2: The Conditional Arithmetic Operation
# Create a 1D array of 10 random integers with values between 1 and 20.
# Create a new array from this one using np.where():
# If a number in the original array is less than 10, the new array's value at that position should be original_value * 100.
# If the number is 10 or greater, the new value should be original_value - 10.
# Print the original array and the new, conditionally-calculated array.


arr_1d = np.random.randint(1,21,(10))
print(arr_1d)
conditioned_arr = np.where(arr_1d<10, arr_1d*100, arr_1d-10)
print(conditioned_arr)

print("\n"*15)

# Question 3: The Sort-and-Stack
# Create a 4x3 matrix named matrix_A of random integers (values 1-20).
# Create another 4x2 matrix named matrix_B of random integers (values 1-20).
# Sort matrix_A column-wise (top to bottom).
# Sort matrix_B row-wise (left to right).
# Horizontally stack (hstack) the sorted matrix_A and the sorted matrix_B to create a new 4x5 matrix.
# Print the final 4x5 matrix.

matrix_A = np.random.randint(1,21, (4,3))
matrix_B = np.random.randint(1,21, (4,2))
print(f"Matrix A: \n{matrix_A}")
print(f"Matrix B: \n{matrix_B}")

sorted_col_matrix_A = print(f"Sorted columnn wise matrix_A: \n{np.sort(matrix_A, axis=0)}")  
sorted_row_matrix_B = print(f"Sorted row wise matrix_B: \n{np.sort(matrix_B, axis=1)}")

h_stacked_matrix = np.hstack((matrix_A, matrix_B))
print(h_stacked_matrix)









print("\n"*15)




# Question 4: The "Find and Delete"
# Create a 1D array containing 20 random integers with values between 1 and 10.
# Find all the indices where the value of the array is greater than 8.
# Use this array of indices to delete all those elements from the original array.
# Print the original 20-element array and the final, filtered array.


arr_1d = np.random.randint(1,11, (10))
print(f"Original array: {arr_1d}")
indices = np.where(arr_1d>8)
print(f"Indices where element > 8: {np.where(arr_1d>8)}")
print(f"Final array after deleting elements at that indices: {np.delete(arr_1d, indices)}")


print("\n"*15)
# Question 5: The "Border"
# Create a 7x7 matrix filled with all zeros, using np.zeros().
# Modify this matrix in place (without creating a new one) to set the "border" elements (the first row, last row, first column, and last column) all to the value 1. The inner 5x5 part should remain all zeros.
# Print the final 7x7 matrix.

all_zeroes = np.zeros((7,7), dtype=int)
print(all_zeroes)

# condition = np.where([all_zeroes[0, :] or all_zeroes[6,:] or all_zeroes[:,0] or all_zeroes[:,6]]) 
# print(condition)          
for i in range(7):
    if i == 0 or i == 6:
        all_zeroes[i] = np.array([1, 1, 1, 1, 1, 1, 1])
    else:
        all_zeroes[i][0] = 1
        all_zeroes[i][6] = 1


print(all_zeroes)        

