import pandas as pd


nr = pd.read_csv("newratings.csv", usecols=['user_id','book_id','rating'])
print(type(nr.user_id[100]))