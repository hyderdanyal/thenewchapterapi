import pandas as pd
from searchpageResponse import *
import json

def searchpage(search):
    books=pd.read_csv('dataset/newbooks.csv',encoding='latin-1')
    
    s=books[books['book_id']==search]
    
    titles=s['title']
    bk_id=s['book_id']
    url=s['image_url']
    des=s['desc']
    
    data=[]
    
    for i in range(len(s)):
        
        search=searchpageResponse(titles.iloc[i],str(bk_id.iloc[i]),url.iloc[i],des.iloc[i])

        search=json.dumps(search.__dict__)
        search=json.loads(search)
        data.append(search)
    
    return data
  
