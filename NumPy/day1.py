import numpy as np
import time 

#creating array from list

array_1d = np.array([1,2,3])
print(array_1d)

array_2d = np.array([[1,2,3],[2,3,4]])
print(array_2d)


#list vs array
list_py = [1,2,3]
print("Mutiplication: ", list_py * 2)   #[1,2,3,1,2,3] 
arrayMuly_py = np.array([1,2,3])
print("Mutiplication: ", arrayMuly_py * 2)  #[2 4 6]

start = time.time()
list_py = [i*2 for i in range(1000000)]
print("Total time list: ", time.time()-start)


start = time.time()
arr_py = np.arange(1000000) * 2
print("Total time array in num_py : ", time.time()-start)

#array from scratch

arr_zeroes = np.zeros((3,4))
print(f"Array zeroes: \n {arr_zeroes}")

arr_1s = np.ones((3,4))
print(f"Array of 1s: \n {arr_1s}")

arr_constant = np.full((3,4), 7)
print(f"Array of constants: \n {arr_constant}")

rand_arr = np.random.random((2,3))
print(f"random vals: {rand_arr}")

arr = np.random.random((2,3))
print(f"more than 1 d: {arr}")
 
arr_seq = np.arange(0, 10, 2)
print(f"Sequence: {arr_seq}")

rand_arr_ints = np.random.randint(0,9,(3,3))
print(f"For random integers array: {rand_arr_ints}")

#vector, matrices, tensor: vector is 1d array, matrices is 2d array

vector = np.array([[[1,2], [3,4], 
                    [5, 6], [6,7], 
                    [9, 10], [10, 11]]])

# print(vector)


#array props:
arr = np.array([[1,2,3], [2,3,4]])

print("shape:", arr.shape)  #(rows, column)
print("dimension: ", arr.ndim)   # dimensions, 1d, 2d, 3d
print("size: ", arr.size)  #number of elemets


#array reshape
arr = np.arange(6)  #1d array
print("Origianl arr: ", arr)  #[0 1 2 3 4 5]

reshaped = arr.reshape((2,3))    #rows * columns 
#[[0 1 2]
# [3 4 5]]
print("Reshaped array: \n", reshaped)

reshaped = arr.reshape((3,2))
print("reshaped again: \n", reshaped)

arr = arr.flatten()
print(arr)


raveled = arr.ravel()
print(raveled, "\n")



#diff bw ravel and flatten, ravel works on the of array, while flatten makes a copy of it:
arr = np.array([[1,2], 
                [3,4]])


r = arr.ravel()
f = arr.flatten()

r[0] = 10
f[0] = 20

print(f"Og arr: {arr}")  #yeh chnage huvi hogi, instead of 1, at [0], its 10
print(f"Raveled: {r}")  #[10 2 3 4]
print(f"Flattened: {f}\n") #[20 2 3 4]

# transpose 
arr_for_trans = np.array([[0,1,2], [1,2,3], [3,4,5]])  #for matrices with random vals, ints
transposed = arr_for_trans.T
print("\nArray for transpose: \n", arr_for_trans)
print(f"\nTransposed array: \n {transposed}")