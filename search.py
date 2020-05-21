import pandas as pd
from searchResponse import *
import json


def searchbook(searchvalue):
    df = pd.read_csv('dataset/newbooks.csv', encoding="ISO-8859-1")

    books = df[df.apply(lambda row: row.astype(
        str).str.contains(searchvalue, na=False).any(), axis=1)]

    # print(books)

    titles = books['title']
    bk_id = books['book_id']
    url = books['image_url']
    des = books['desc']

    data = []
    for i in range(len(books)):
        gen = SearchResponse(titles.iloc[i], str(
            bk_id.iloc[i]), url.iloc[i], des.iloc[i])

        gen = json.dumps(gen.__dict__)
        gen = json.loads(gen)
        data.append(gen)
    return data
