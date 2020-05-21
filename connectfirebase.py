import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

data = []
cred = credentials.Certificate('book-cred.json')
firebase_admin.initialize_app(cred)


def bookid(name, uid):
    # Use a service account

    db = firestore.client()

    # name='danyal hyder'
    # uid='ATKABiBicvcuRZvoqkqO4Ru8gDW2'
    # Add a new doc in collection 'cities' with ID 'LA'
    doc_ref = db.collection(u'ratings').where(u'book', u'==', True).stream()
    # docs = doc_ref.where(u'book', u'==', u'true')
    # print(u'Document data: {}'.format(doc_ref.to_dict()))

    # docs = db.collection_group(u'ratings')\
    #     .where(u'book', u'==', u'true')
    # doc_ref = docs.stream()
    # for doc in doc_ref:
    #     print(u'{} => {}'.format(doc.id, doc.to_dict()))
    # data.append(doc.id)
    # print(u'{} => {}'.format(doc.id, doc.to_dict()))
    # print(data)
# def returndata():
#   return data
    ref = db.collection_group(u'review')\
        .where(u'reviewed', u'==', True).order_by('user_id')
    docs = ref.stream()
    for doc in docs:
        # print(u'{} => {}'.format(doc.id, doc.to_dict()))
        data.append(doc.to_dict())
        # data2 = data2.to_dict()

    print(type(data), data)
    df = pd.DataFrame(data)
    df1 = df[['user_id', 'book_id', 'rating']]
    print(df1)

    # print(type(data[1]), data[1])

    # print(type(data[1]['user_id']), data[1]['user_id'])


bookid('hadi hyder', 'yC7YrZxDkJSTPx8RuaPrA8yMOkh1')
