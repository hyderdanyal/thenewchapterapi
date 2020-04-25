# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:37:15 2020

@author: LENOVO
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

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

    # img_url=books['image_url']
    titles = books['title']
    indices = pd.Series(books.index, index=books['title'])

    # Function that get book recommendations based on the cosine similarity score of book authors
    def authors_recommendations(title):
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:21]
        book_indices = [i[0] for i in sim_scores]
        # return titles.iloc[book_indices]
        tup1=('title')
        tup2=(titles.iloc[book_indices])
        res= dict(zip(tup1,tup2))
        print("Dict: " +str(res))

    return authors_recommendations(title).head(20)   
    
