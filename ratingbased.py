import pandas as pd
import json
import io
from ratingResponse import RatingResponse


def ratingbased():
    books = pd.read_csv('dataset/newbooks.csv', encoding="ISO-8859-1")

#    books.head()

#    books.shape

    sorted_books = books.sort_values(by=["average_rating", "ratings_count"],
                                     axis=0, ascending=False, kind="quicksort", na_position="last")
    titles = sorted_books['title']
    g_id = sorted_books['book_id']
    url = sorted_books['image_url']
    des = sorted_books['desc']

    indices = pd.Series(sorted_books.index, index=sorted_books['title'])

    data = []
    for i in indices[:15]:
        author = RatingResponse(titles.iloc[i], str(
            g_id.iloc[i]), url.iloc[i], des.iloc[i])
        author = json.dumps(author.__dict__)
        author = json.loads(author)
        data.append(author)

    return data
