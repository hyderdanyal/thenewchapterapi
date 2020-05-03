
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from authorResponse import AuthorResponse
import jsonpickle
import json


def authorbased(title):
    books = pd.read_csv('dataset/books.csv', encoding = "ISO-8859-1")
    books.head()

    books.shape

    ratings = pd.read_csv('dataset/ratings.csv', encoding = "ISO-8859-1")
    ratings.head()

    book_tags = pd.read_csv('dataset/book_tags.csv', encoding = "ISO-8859-1")
    book_tags.head()

    tags = pd.read_csv('dataset/tags.csv')
    tags.tail()

    tags_join_DF = pd.merge(book_tags, tags, left_on='tag_id', right_on='tag_id', how='inner')
    tags_join_DF.head()

    to_read = pd.read_csv('dataset/to_read.csv')
    to_read.head()



    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(books['authors'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


    titles = books['title']
    g_id=books['goodreads_book_id']
    url=books['image_url']
    des=books['desc']

    indices = pd.Series(books.index, index=books['title'])

    # Function that get book recommendations based on the cosine similarity score of book authors
    def authors_recommendations(title):
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:21]
        book_indices = [i[0] for i in sim_scores]
        #for i in book_indices:
        data=[]
        for i in book_indices:
            author=AuthorResponse(titles.iloc[i],str(g_id.iloc[i]),url.iloc[i],des.iloc[i])
            author=json.dumps(author.__dict__)
            author=json.loads(author)
            data.append(author)
        
        # data=AuthorResponse(titles.iloc[book_indices].tolist(),g_id.iloc[book_indices].tolist(),url.iloc[book_indices].tolist())
        dataset=data   
        
        # print(dataset)
        return dataset         
        
        # print(books[books["goodreads_book_id","title"]]==titles.iloc[book_indices])
        #return titles.iloc[book_indices]

    return authors_recommendations(title)
    # return authorbased(title)
