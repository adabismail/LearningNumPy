import pandas as pd

df = pd.DataFrame([[1,2,3], [4,5,6,], [7,8,9]], columns=["a", "b", "c"], index=["alpha", "beta", "gamma"])


print(df) #shows entire df
print("\n")
print(df.head(2))   #df.head() by default prints first 5 rows of df, we can specify by df.head(3), shows first 2 rows
print("\n")
print(df.tail(2))  #shows last 2 rows


print(df.columns)   #Index(['a', 'b', 'c'], dtype='object')
print(df.index)    #Index(['alpha', 'beta', 'gamma'], dtype='object')

print(df.columns.tolist())    # ['a', 'b', 'c']
print(df.index.tolist())    # ['alpha', 'beta', 'gamma']

df = pd.read_csv("pokemon.csv")
print(df)


