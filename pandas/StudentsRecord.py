import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Priya", "Neha", "Rohan", "Simran", "Karan", "Pooja"],
    "Age": [21, 22, 20, 21, 23, 20, 22, 21],
    "Math": [78, 92, 65, 88, 55, 95, 69, 84],
    "Python": [85, 88, 72, 91, 62, 93, 75, 79],
    "ML": [72, 95, 68, 84, 58, 97, 71, 88],
    "English": [90, 91, 70, 87, 60, 96, 68, 82]
}

df = pd.DataFrame(data)

"Display the first 5 rows."
print(df.head(5))


"Find the number of rows and columns."
print(df.shape)

"Display the column names."
print('Column Names:',df.columns)

"Check whether there are any missing values."
print(df.isnull())

"Find the average marks in Math."
print(df["Math"].mean())


"Find the highest marks in Python."
print(df["Python"].max())

"Find the average marks of every subject."
print(df[["Math","Python","ML","English"]].mean())

"""
3. Filtering
Find all students who:

scored more than 80 in Math
scored more than 80 in both Math AND Python
scored more than 90 in at least one subject"""