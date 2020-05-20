import pandas as pd
from genreResponse import *
import json

def genre(genre):
    books=pd.read_csv('dataset/newbooks.csv',encoding='latin-1')

    g=books[books['genre']==genre]
    g=g.head(24)
    
    titles=g['title']
    bk_id=g['book_id']
    url=g['image_url']
    des=g['desc']
    
    data=[]
    
    for i in range(len(g)):
        
        gen=GenreResponse(titles.iloc[i],str(bk_id.iloc[i]),url.iloc[i],des.iloc[i])

        gen=json.dumps(gen.__dict__)
        gen=json.loads(gen)
        data.append(gen)
    return data
   
