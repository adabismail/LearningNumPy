import random

# rows = 3
# columns = 3

# # random_matriz = [
# #                  [1,2],
# #                  [3,4]
# #                  ]

# matrix = [3][5]
# for i in range(rows):
#     for j in range(columns):
#         rand_number = random.randint(1,5)
#         matrix[i][j] = rand_number

# print(matrix)        

matrix = [2][2]

for i in range(2):
    for j in range(2):
        matrix[i][j] = random.randint(2,4)

print(matrix)        