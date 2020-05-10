import pandas as pd
from searchpageResponse import *
import json

def searchpage(search):
    books=pd.read_csv('dataset/newbooks.csv',encoding='latin-1')
    
    s=books[books['book_id']==search]
    # s=s.head(1)
    # print(g['title'],g['book_id'],g['image_url'],g['desc'])
    titles=s['title']
    bk_id=s['book_id']
    url=s['image_url']
    des=s['desc']
    # print(titles,ck)
    # indices = pd.Series(g.index, index=g['title'])
    # print(indices)
    data=[]
    # print(titles)
    for i in range(len(s)):
        
        search=searchpageResponse(titles.iloc[i],str(bk_id.iloc[i]),url.iloc[i],des.iloc[i])

        search=json.dumps(search.__dict__)
        search=json.loads(search)
        data.append(search)
    # print(data)
    return data
# searchpage(2921)    
