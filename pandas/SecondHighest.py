import pandas as pd

person = pd.DataFrame({
    "Id": [1,2,3],
    "salary": [1000,2000,3000],
})

print(person["salary"].nLargest(2).iloc[-1])