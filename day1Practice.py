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
