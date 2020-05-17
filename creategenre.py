import pandas as pd
import math

tags='dataset/book_tags1.csv'
df_tags=pd.read_csv(tags, usecols=['goodreads_book_id','tag_id','count'])
tags1='dataset/tags.csv'
df_tags1=pd.read_csv(tags1, usecols=['tag_id','tag_name'])

df_tags=df_tags.dropna()
unique =df_tags.goodreads_book_id.unique()
print(unique)



h=0
g=[]
t=[]
c=[]
print(len(g),len(t),len(c))
for i in unique:

  
  gr=df_tags.loc[df_tags['goodreads_book_id'] == i]
  
    
  g.append(i)
  t.append(gr['tag_id'].iloc[0])
  c.append(gr['count'].max())
  
  
    
print(len(g),len(t),len(c))
updated={
  'goodreads_book_id':g,
  'tag_id':t,
  'count':c
}
a=pd.DataFrame(updated)
print(a)

pd.set_option("display.max_rows", None, "display.max_columns", None)
tags_join_DF = pd.merge(a,df_tags1, on='tag_id',how='left')

tags_join_DF.to_csv('genre.csv',index=False)

genre='genre.csv'
genre=pd.read_csv(genre, usecols=['goodreads_book_id','tag_id','count','tag_name'])
genre
