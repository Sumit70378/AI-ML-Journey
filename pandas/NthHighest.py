employee = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Joe", "Henry", "Sam", "Max", "Alice"],
    "salary": [85000, 80000, 60000, 70000, 80000]
})

N = 2


df_nth = employee["salary"].drop_duplicates().nlargest(N)

if len(df_nth) < N:
        sal = None
else:
        sal = df_nth.iloc[-1]


print(sal)