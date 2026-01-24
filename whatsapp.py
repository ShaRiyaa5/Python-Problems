import pandas as pd
from streamlit import columns

db = pd.read_csv("whatsapp_chat.csv")
print(db)
print(db.head())
print(db.tail(2))
print(db.info())
print(db.describe())
print(db.shape) #() should not use
print(db.columns)
print(db.sort_values(by = 'days'))
print(db.dtypes)
print(db.groupby('months'))
print(db.query("hours < 1"))
print(db["hours"])
print(db.iloc[5])
print(db.iloc[135:145])
print(db.iloc[5,3])
print(db.query("hours>2").value_counts())
print(db["names"].value_counts())
print(db["hours"].value_counts())
print(db["names"].unique())

