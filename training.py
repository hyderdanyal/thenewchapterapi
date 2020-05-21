from surprise import Reader, Dataset, SVD, accuracy
from surprise.model_selection import cross_validate, KFold
import numpy as np
import pandas as pd
import pickle
from scipy.sparse.linalg import svds
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


data1 = []
cred = credentials.Certificate('book-cred.json')
firebase_admin.initialize_app(cred)


def training():

    db = firestore.client()
    doc_ref = db.collection(u'ratings').where(u'book', u'==', True).stream()

    ref = db.collection_group(u'review')\
        .where(u'reviewed', u'==', True).order_by('user_id')
    docs = ref.stream()
    for doc in docs:
        data1.append(doc.to_dict())
    # print(type(data), data)
    df = pd.DataFrame(data1)
    df1 = df[['user_id', 'book_id', 'rating']]
    # print(df1)

    ratingss = pd.read_csv('dataset/ratings.csv',
                           usecols=['user_id', 'book_id', 'rating'])
    # print(ratings.head(5))
    ratings = pd.concat([ratingss, df1])
    # print(new)
    ratings['user_id'] = ratings['user_id'].apply(str)

    n_users = ratings.user_id.unique().shape[0]
    n_books = ratings.book_id.unique().shape[0]
    print('Number of users = ' + str(n_users) +
          ' | Number of books = ' + str(n_books))

    Ratings = ratings.pivot(
        index='user_id', columns='book_id', values='rating').fillna(0)
    # Ratings.head()

    R = Ratings.to_numpy()
    user_ratings_mean = np.mean(R, axis=1)
    Ratings_demeaned = R - user_ratings_mean.reshape(-1, 1)

    sparsity = round(1.0 - len(ratings) / float(n_users * n_books), 3)
    # print ('The sparsity level of MovieLens1M dataset is ' +  str(sparsity * 100) + '%')

    U, sigma, Vt = svds(Ratings_demeaned, k=50)

    sigma = np.diag(sigma)
    # sigma

    all_user_predicted_ratings = np.dot(
        np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

    preds = pd.DataFrame(all_user_predicted_ratings, columns=Ratings.columns)

    reader = Reader()

    # Load ratings dataset with Dataset library
    data = Dataset.load_from_df(
        ratings[['user_id', 'book_id', 'rating']], reader)

    # Split the dataset for 5-fold evaluation
    kf = KFold(n_splits=5)
    svd = SVD()

    for trainset, testset in kf.split(data):

        # train and test algorithm.
        svd.fit(trainset)
        predictions = svd.test(testset)

        # Compute and print Root Mean Squared Error
        accuracy.rmse(predictions, verbose=True)

    trainset = data.build_full_trainset()
    svd.fit(trainset)
    print('Data Trained Successfully')
    with open('model_pickle', 'wb') as f:
        pickle.dump(svd, f)


training()
