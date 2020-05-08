import pandas as pd
import json
import io
from timeResponse import TimeResponse



def timebased():
   books=pd.read_csv('dataset/books.csv', encoding = "ISO-8859-1")

   books.head()

   books.shape

   sorted_books=books.sort_values(by=["original_publication_year","ratings_count", "average_rating"],
    axis=0, ascending=False , kind="quicksort", na_position="last")
#    sorted_books=sorted_books[:25] 
   titles = sorted_books['title']
   g_id=sorted_books['goodreads_book_id']
   url=sorted_books['image_url']
   des=sorted_books['desc']

   indices = pd.Series(sorted_books.index, index=sorted_books['title'])

   data=[]
   for i in indices[:25]:
        author=TimeResponse(titles.iloc[i],str(g_id.iloc[i]),url.iloc[i],des.iloc[i])
        author=json.dumps(author.__dict__)
        author=json.loads(author)
        data.append(author) 

    # dataset=data
   return data

