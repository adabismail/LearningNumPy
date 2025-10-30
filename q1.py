import random


def func(numbers_list, flag):
    greater_list = []
    smaller_list = []
    for i in numbers_list:
        if (i>flag):
            greater_list.append(i)
        else:
            smaller_list.append(i)
    print(f"Numbers greater than {flag}: {greater_list}")
    print(f"Numbers smaller than {flag}: {smaller_list}")
    
numbers_list = []

length_list = random.randint(10,20)
flag = random.randint(10,20)

for i in range(length_list):
      numbers_list.append(random.randint(1,20))

print(f"Original list {length_list}: {numbers_list}")
func(numbers_list, flag)