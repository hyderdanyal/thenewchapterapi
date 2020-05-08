import pandas as pd
from genreResponse import *
import json

def genre(genre):
    books=pd.read_csv('dataset/newbooks.csv',encoding='latin-1')

    g=books[books['genre']==genre]
    g=g.head(20)
    # print(g['title'],g['book_id'],g['image_url'],g['desc'])
    titles=g['title']
    bk_id=g['book_id']
    url=g['image_url']
    des=g['desc']
    # print(titles,ck)
    # indices = pd.Series(g.index, index=g['title'])
    # print(indices)
    data=[]
    # print(titles)
    for i in range(len(g)):
        # print("asasasas",i)
        # print(titles.iloc[i])
        # print(bk_id.iloc[i])
        # print(url.iloc[i])
        # print(des.iloc[i])
        gen=GenreResponse(titles.iloc[i],str(bk_id.iloc[i]),url.iloc[i],des.iloc[i])

        gen=json.dumps(gen.__dict__)
        gen=json.loads(gen)
        data.append(gen)
    return data
# genre('fiction')    
