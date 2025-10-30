import random

data_set = random.randint(5,10)


heights_m = [(random.randint(100,200)/100) for i in range(data_set)]
print(heights_m)

weights_kg = [random.randint(55,100) for i in range(data_set)]
print(weights_kg)

bmi = [round(heights_m[i]*weights_kg[i],2) for i in range(data_set)]

print(bmi)