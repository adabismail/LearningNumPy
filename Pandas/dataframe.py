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


# data = [
#     ['John', 'Anna', 'Peter', 'Linda'],
#     [28, 34, 29, 42],
#     ['New York', 'Paris', 'Berlin', 'London'],
#     [65000, 70000, 62000, 85000]
# ]
# df2 = pd.DataFrame(data, columns=["Name", "Age", "City", "Salary"])
# print(df2)


#locating columns
print("\n")
print(df[["Name", "Age"]])   #provide a list of list to target more than one column
print("\n")

#new column
df["Designation"] = ["doc", "eng", "doc", "eng"]  #provide a list
print(df)
print("\n")


#removing col
df.drop(columns=["Designation"], axis=0, inplace=True)   #can provide a list to remove multiple
print(df)     #we cant do print(df(....., inplace=True)), like udgar hi print nai hoga, itll print None
print("\n")
df.insert(1, "Gender", ["f", "m", "m", "m"])    #insert adds col at a pos., takes pos, col name(strig), and what to add(list)


#removing row
df.drop(index=0, axis=0, inplace=True)   #dropping row 0, toh ab start hoga 1 row se. can provide a list too
print(df)
print("\n")


df["Designation"] = ["Doc", "Engg", "Doc"]
print(df)
print("\n")


#adding row 
df.loc[0] = ["Adab", "m", 21, "Srinagar", 101001010, "Engg"]   #df.loc[len(df)] to add at last pos.
print(df)
print("\n")


#to locate rows
print("\n")
print(df.loc[1:2])

print("\n"*10)
print(df)


#selecting col based on cond
print("\nSelection rows based on cond., with age > 30 and designation = doctor")
print(df[(df["Age"]>30) & (df["Designation"]=="Doc")])


