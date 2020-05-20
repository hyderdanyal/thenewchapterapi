import pandas as pd


ratings = pd.read_csv('dataset/ratings.csv', encoding = "ISO-8859-1", usecols=['user_id'])
lenght1=len(ratings)
gender=pd.read_csv('dataset/users.csv',sep='\t', encoding='latin-1',usecols=['gender'])


lenght3=len(ratings)

ratings.drop_duplicates(subset ="user_id", 
                     keep = 'first', inplace = True) 
print(lenght1,lenght3)



gender.to_csv('out.csv',index=False)

    