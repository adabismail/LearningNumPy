import pandas as pd
import numpy as np

#finding missing data 
data = {
    'A': [1, 2, 3, np.nan, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, 3, np.nan, 5]
}

df = pd.DataFrame(data)
print(f"DataFrame: \n{df}")

print(f"\nAs a T/F value: \n{df.isna()}")

#to see how many null in rows and cols
print(f"\nNaN vals in each col: \n{df.isna().sum()}")    #axis=0 as default as column, can change axis=1 to rows
print(f"\nNaN vals in each row: \n{df.isna().sum(axis=1)}") 
print("\n") 

# print(df.isna().any())  yeh check kare ga ki cols mei null hai ya nai, true ret if col has, else false
#A    True
#B    True
#C    True
#D    True

print(df)

#removing nan rows and cols : df.dropna()

#drops all the rows(by default), that has any nan val
print(f"Dropped rows 1,3,4. left df:\n {df.dropna(axis=0)}\n")
print(f"Dropped col. A,C,D: left df:\n {df.dropna(axis=1)}\n")

#threshold: matlab aisa rows/cols matlab jin mei minimum thresh hogai, woh remove nai hogai??

print(f"With thresh=2, only those rows stay that have 2 or more non-nan vals: \n{df.dropna(thresh=2)}\n")

#filling the missing data:
print(f"data frame: \n {df}\n")

print(f"after filling 0s in nan places: \n: {df.fillna(0)}\n")     #this is a copy only, we have to use inplace=True, to show chaneg in the actual dataframe


#print(df)  this will still print df with nan vals
#in order to make changes in the original df completely
#df.fillna(0, inplace=True)  
#print(f"after filling 0s in nan places: \n{df}")

#with apni marzi ki vals:
values = {'A': 0, 'B': 100, 'C': 200, 'D':400}
print(f"Og df: \n{df}\n")
print(f"fillings cols with: {values}\n")
print(f"filling cols withh values: \n{df.fillna(value=values)}\n")    #this is a copy only, we have to use inplace=True, to show chaneg in the actual dataframe


#filling vals with mean
# print(df.fillna(np.mean(df, axis=0)))  #look up tomorrow

print(f"Filling with mean vals: \n{df.fillna(df.mean())}")


#mean of particular col:
#df['A'].mean()