import pandas as pd
import numpy as np


data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}

df = pd.DataFrame(data)
print(df)

data = [
    ['John', 'Anna', 'Peter', 'Linda'],
    [28, 34, 29, 42],
    ['New York', 'Paris', 'Berlin', 'London'],
    [65000, 70000, 62000, 85000]
]

# df2 = pd.DataFrame(data, columns=["Name", "Age", "City", "Salary"])
# print(df2)


#locating columns
print(df[["Name", "Age"]])   #provide a list of list to target more than one column


#new column
df["designation"] = ["doc", "eng", "doc", "eng"]  #provide a list
print(df)
print("\n")


#removing col
df.drop(["designation", "Salary"], axis=1, inplace=True)
print(df)
print("\n"*10)
#remiving row
df.drop(0, axis=0, inplace=True)
print(df)
print("\n"*5)
df["Designation"] = ["Doc", "Engg", "Doc"]
print(df)

#to locate rows
print("\n")
print(df.loc[1:2])