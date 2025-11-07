import pandas as pd
import numpy as np

# --- The Data ---
data = {
    'StudentID': ['Student_A', 'Student_B', 'Student_C', 'Student_D', 'Student_E', 'Student_F', 'Student_G', 'Student_H'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Subject': ['Math', 'English', 'Math', 'Science', 'English', 'Math', 'Science', 'English'],
    'Score': [85.0, 92.0, np.nan, 78.0, 95.0, 68.0, 88.0, np.nan],
    'Category': ['X', np.nan, 'Y', 'X', 'Y', np.nan, 'X', 'Y']
}

df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
print("\n")
# Question 1: The Index and Position Challenge
# Set the StudentID column as the index of the DataFrame.
# Using .loc, select all data for 'Student_C' and 'Student_G'.
# From the resulting 2-row DataFrame, use .iloc to select and print only the data in the first row and the last two columns.

df = df.set_index("StudentID")
df2 = df.loc[['Student_C', 'Student_G']]
print(f"Data for Student_C and Student_G:\n {df2}")
print("\n")
print(f"print only the data in the first row and the last two columns: {df2.iloc[[0], [-2,-1]]}")
print("\n"*10)


# Question 2: The Two-Part NaN Fill
# Create a new column named 'Score_Filled' that is a copy of the original 'Score' column.
# Fill all NaN values in the 'Score_Filled' column with the mean of the entire 'Score_Filled' column.
# Create another new column named 'Category_Filled' that is a copy of the 'Category' column.
# Fill all NaN values in the 'Category_Filled' column using the forward-fill method (ffill).
# Print the final DataFrame, showing the four new and old columns (Score, Score_Filled, Category, Category_Filled).


# print(f"Data frame: \n {df}")

# df.insert(column='Score_Filled', value=df['Score'], loc=len(df.columns))  #After insertion new column

# df = df.fillna(value=df['Score_Filled'].mean())
# print(df)
# print(f"Score_Filled with mean vals: \n {df}")
# df.insert(value=df['Category'], loc=len(df.columns), column='Category_Filled')
# print(f"After insertion new column 'Category_Filled:\n {df}")

# df = df['Category_Filled'].ffill(axis=0)


# Question 3: The Conditional Column Creator
# Add a new column to the DataFrame named 'Status', and initialize all its values to the string 'Incomplete'.
# Using a boolean mask, find all rows where the 'Score' is greater than 80 and set their 'Status' to 'High-Performer'.
# Using a separate boolean mask, find all rows where the 'Score' is less than 70 and set their 'Status' to 'Needs-Support'.
# Print the final DataFrame, including the new 'Status' column.

print("\n"*10)
print(df)
values = ["Incomplete"] * len(df)
df.insert(column="Status", value=values, loc=len(df.columns))
print(df)
print("\n")

# print(df[df['Score']>80])
# mask = df['Score'] > 80
# print(mask)

df.loc[df['Score']>80, 'Status'] = "High Performer"
df.loc[df['Score']<70, 'Status'] = "Needs help"

print(df)








# Question 4: The Strict Cleaner
# Drop all rows from the DataFrame that do not have at least 4 non-NaN values.
# Print the resulting, smaller DataFrame.
print("\n"*10)
print(df)
print("\n"*1)
df = df.dropna(axis=1, thresh=4)
print(df)



# Question 5: The "Above Average" Report
# First, run df.describe() on the DataFrame to get the summary statistics.
# From those statistics, find the value for the 75th percentile (Q3) of the 'Score' column.
# Using that 75th percentile value, filter and print all rows from the original DataFrame where the 'Score' is strictly greater than the 75th percentile.
print("\n"*10)
print(df.describe())





# Question 6: The "Frankenstein" DataFrame
# Using .iloc, select and delete the row at position 3 (the one for 'Student_D').
# Delete the entire 'Category' column.
# Insert a new column at position 1 (right after StudentID) named 'On_Probation', and set all its values to False.
# Add a new row for 'Student_I' (Name: 'Ivan', Subject: 'Math', Score: 99.0, On_Probation: False) to the very end of the DataFrame.
# Print the final, modified DataFrame.

print("\n"*10)
data = {
    'StudentID': ['Student_A', 'Student_B', 'Student_C', 'Student_D', 'Student_E', 'Student_F', 'Student_G', 'Student_H'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Subject': ['Math', 'English', 'Math', 'Science', 'English', 'Math', 'Science', 'English'],
    'Score': [85.0, 92.0, np.nan, 78.0, 95.0, 68.0, 88.0, np.nan],
    'Category': ['X', np.nan, 'Y', 'X', 'Y', np.nan, 'X', 'Y']
}
df = pd.DataFrame(data)

df = df.drop(df.iloc[[3]].index)
df = df.drop(columns='Category')
df.insert(column="On_Probation", loc=0, value=False)
df.loc[len(df)] = ['Student_I', False, 'Ivan','Math', 99.0]

print(df)

