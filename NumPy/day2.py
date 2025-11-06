#NUMPY ARRAY OPERATIONS


import numpy as np


#arr = np.array([1,2,3], dtype=float), takes 1 or 2 inputs
#arr = np.arange(1,11,2, dtype=float)


arr = np.arange(1, 11)  
print(f"Printing array: {arr}")    #[1 2 3 4 5 6 7 8 9 10]
print(f"with slicing: {arr[3:7]}")    #[4 5 6 7]


# print(f"With step: {arr[[i for i in range(len(arr)) if arr[i]%2==0]]}")
# print(arr%2) yaha iterate hoga ahrr elemts of array, then print the value ->
# [1 0 1 0 1 0 1 0 1 0]



# now if hum print(arr%2 == 0), toh yeh boolean print hoga -> [False True False True ......]
# this created a boolean mask

# so optimized way to pritn even numebrs
# print(f"Even numebrs: {arr[arr % 2 == 0]}), keeps boolean val True, prints them, discards Fal eones


print(f"Array with steps: {arr[0:10:2]}")  #Array with steps: [ 1  4  7 10]

print(f"Array with negative indexing: {arr[-1]}")

print("\3"*5)

#2D ARRAY

arr_2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(f"Array 2d :\n {arr_2d}")
print(f"Specific elem row1, col2: {arr_2d[1, 2]}")   #row 1 , columns 2, indexing starts from 1

print(f"Entire row: {arr_2d[0]}")  #0th row [1 2 3]
print(f"Entire column: {arr_2d[:, 0]}")   #0th column [1 4 7]



#SORTING
unsorted = np.random.randint(1,11, (10))
print(f"unsorted array: {unsorted}")

sorted = np.sort(unsorted)
print(f"Sorted array: {sorted}\n")

unsorted_2d = np.random.randint(1,11, (3,2))
print(f"Unsorted 2d array: {unsorted_2d}")

#abb iso sort karne ke 2 ways, row wise(left to right) and column wise(top to bottom)
#axis = 0 toh column wise, axis=1 matlab row wise


sorted_2d_col = np.sort(unsorted_2d, axis=0)   #0 matlab col
sorted_2d_row = np.sort(unsorted_2d, axis=1)    # 1 matlab row

print(f"Column wise: {sorted_2d_col}\n Row wise: {sorted_2d_row}")

print("\n"*6)



#Filtering array

numbers = np.arange(1,11)     #[1 2 3 4 5 6 7 8 9 10]
print(f"Numbers array: {numbers}")

# print(numbers[0]%2)

# print(f"Numbers divisible by 2 will give 0: {numbers%2}")   #[1 0 1 0 1 0 1 0 1 0]
# print(numbers[numbers%2])   [[2 1 2 1 2 1 2 1 2 1]  , match with the array above [1 0 1 0....], prints numbers[1] and numbers[0] alternatively
even_numbers = numbers[numbers%2 == 0]
print(f"Evem numbers: {even_numbers}")



#MASK:
# mask is basiclaly a boolean array [True False True False .....] type shi
# now for exxample: 

mask1 = numbers > 5  #this will create an array of the og numbers array that was [ 1  2  3  4  5  6  7  8  9 10], now numbers
#greater than 5 will have a true val else will have false: [False False False False False  True  True  True  True  True]
print(mask1)

# for this below, thi smask will hve truw val for even numbers else fasle, [False  True False  True False  True False  True False  True]
# || ly for this below
mask2 = numbers % 2 == 0
print(mask2)

#so efficinetly we can print even numbers or numbers > 5

print(f"Even numbers: {numbers[numbers%2==0]}")
print(f"Numbers > 5: {numbers[mask1]}")   

#the true fasle list as an array is given as an index to the og list, it accepts the val stored at true, discards val at false

print("\n"*6)

#FANCY INDEXING VS np.where()::
print(f"Numbers array is : {numbers}")
numbers_list = [1,2,3,4,5,6,7,8,9,10]
print(f"Numbers list is : {numbers_list}")

indices_list = [0,1,2,3,4]
indices_array = np.arange(5)

# print(f"Indices are {indices_list}, and numberes are {numbers_list[indices_list]}")   this wont work since, list indices must be integers or slices, not list
 
print(f"Indices array is {indices_array}, and numberes are {numbers[indices_array]}")
print(f"Indices list is {indices_list}, and numberes are {numbers[indices_list]}")

#so in short list[list_of_indices] not allowd, though array[array_of_indices] and array[list_of_indices], both allowed, itll print item at that index


where_result = np.where(numbers>5)
print(f"Indices where number>5: {where_result}")  #priints an array of indices where numbers > 5
array_greater_5 = numbers[where_result]
print(f"Where results: {array_greater_5}")

#conditional array:
conditional_array = np.where(numbers>5, "t", "f")   #['f' 'f' 'f' 'f' 'f' 't' 't' 't' 't' 't']
print(conditional_array)

#toh yaha basically
# if(condition):   condition here is numbers>5
#    execute(x)    "t"
#else:
#    execute(y)    "f"


print("\n"*6)

#ADDING AND REMOING DATA

arr1 = np.array([1,2,3,4])
arr2 = np.array([2,3,4,5])
print(f"Arr1: {arr1}, Arr2: {arr2}")
added_array = arr1+arr2   
print(f"Added array: {added_array}")   #[3,5,7,9]


concatenated_array = np.concatenate((arr1, arr2))    # [1 2 3 4 2 3 4 5], tuples of arrays
print(f"Concatenated array: {concatenated_array}")

print(f"Copatibility: {arr1.shape == arr2.shape}")   #both shapes same

print("\n" * 7)






#ADDINGD ROWS AND COLUMNS

# original = np.random.randint(1,6, (8))
# print(f"Original array:\n {original}")


# new_col = np.array([4,5])
# with_new_col = np.hstack((original, new_col))
# print(f"Matrix with new column:\n {with_new_col}")


#rows lagta hai horizontal hstack hoga, but woh vertical stack add hota hai so vstack(),imagine ke neeche ek aur row add huva so vstack, and ||ly in columns

original = np.array([[1,2,3], [2,3,4]])   #(rows=2, cols=3)
print("Original array: \n", original)

added_row = np.array([4,6,7])   #([[1,2,3], [2,3,4], [4,6,7]])
added_col = np.array([[0], [9]])   #([[1,2,3,0], [2,3,4,9]])

added_row_array = np.vstack((original, added_row))
added_col_array = np.hstack((original, added_col))

print(f"Array with added row: \n{added_row_array}")
print(f"Array with added col: \n{added_col_array}")



#Deleting 

array = np.arange(0,11)
print(f"array: {array}")
deleted1 = np.delete(array, [0,9,1])   #takes two inputs: the og array and what indices to be deleted
deleted2 = np.delete(array, [3])

print(f"array after deletion using [indices to be deleted, 0,1,9]: {deleted1}")  
print(f"array after deletion only 1 index (3rd index): {deleted2}")

