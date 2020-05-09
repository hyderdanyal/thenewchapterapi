import pandas as pd

# genre = pd.read_csv("dataset/ratings.csv", usecols=['user_id','book_id','rating'])
# genre['user_id']=genre['user_id'].apply(str)
# print(type(genre.user_id[100]))
# newratings=genre.to_csv("newratings.csv")
nr = pd.read_csv("newratings.csv", usecols=['user_id','book_id','rating'])
print(type(nr.user_id[100]))