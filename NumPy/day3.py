import numpy as np
import matplotlib.pyplot as plt


# data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])

print("====SALES====")
print(f"Sample data: \n{sales_data}")
print("\n")
# print(sales_data[:, :3])
# print(sales_data[:, 1:])

sales_per_year = np.sum(sales_data[:, 1:], axis=0)
sales_per_rest = np.sum(sales_data[:, 1:], axis=1)
print(f"Total sales per year, all rest. combined: {sales_per_year}")   #total sales of every rest. each year, this is year wise
print(f"Total sales per rest., all years combined: {sales_per_rest}")   #total sales of each rest., total of all years for each year

# sales_data_pure = sales_data[:, 1:]
# print(sales_data_pure)
# sorted_data = np.sort(sales_data_pure, axis=1)
# print(f"Minimun sales per rest. : {sorted_data[:, 0]}")

print(f"Minimun sales per rest. : {np.min(sales_data[:, 1:], axis=1)}")

plt.figure(figsize=(7,5))
plt.plot(sales_per_year)
plt.title("Total sales per year, all rest. combined")
plt.xlabel("years")
plt.ylabel("Sales")
plt.grid(True)
# plt.show()

print("\n"*15)

vector1 = np.random.randint(1,11,(2,2))
vector2 = np.random.randint(1,11,(2,2))
print(f"vector1:\n {vector1} \n vector2: \n{vector2}\n")


print(f"Vector sum:\n {vector1+vector2}\n")
print(f"Vector mult:\n {vector1*vector2}\n")   #this is nomral mult., item at (0, 0) will mult to item at (0,0)
print(f"Vector dot: \n{np.dot(vector1, vector2)}") 



#Vectorized UPPER:
arr = np.array(["biryani", "pizza", "burger", "paneer"])
#now to upper case
vectorized_upper = np.vectorize(str.upper)
vectorized_arr = vectorized_upper(arr)

# print(vectorized_upper)
print(vectorized_arr)


#BROADCAST

avg_sales = np.round(sales_data[:, 1:] / 12,2)
print(avg_sales)

# mean_per_rest = np.mean(sales_data[:, 1:], axis=1)
# print(mean_per_rest)






