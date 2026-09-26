import pandas as pd
person = pd.DataFrame({
    "personId": [1, 2, 3],
    "lastName": ["Wang", "Alice", "Smith"],
    "firstName": ["Allen", "Bob", "John"]
})
address = pd.DataFrame({
    "addressId": [101, 102],
    "personId": [1, 2],
    "city": ["New York", "London"],
    "state": ["NY", "England"]
})


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    df_merge = pd.merge(person, address, on="personId", how="left")
    df_merge = df_merge[["firstName", "lastName", "city", "state"]]

    return df_merge


result = combine_two_tables(person, address)

print(result)