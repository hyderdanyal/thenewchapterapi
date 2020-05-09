import numpy as np
import pandas as pd

# Reading ratings file
ratings = pd.read_csv('dataset/ratings.csv',  usecols=['user_id', 'book_id', 'rating'])

# Reading users file
users = pd.read_csv('dataset/users.csv', sep='\t', usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])

# Reading movies file
books = pd.read_csv('dataset/newbooks.csv',  usecols=['book_id', 'title', 'genre'])

books.head()

ratings.head()

n_users = ratings.user_id.unique().shape[0]
n_books = ratings.book_id.unique().shape[0]
print('Number of users = ' + str(n_users) + ' | Number of books = ' + str(n_books))

Ratings = ratings.pivot(index = 'user_id', columns ='book_id', values = 'rating').fillna(0)
# Ratings.head()

R = Ratings.to_numpy()
user_ratings_mean = np.mean(R, axis = 1)
Ratings_demeaned = R - user_ratings_mean.reshape(-1, 1)
# Ratings_demeaned

sparsity = round(1.0 - len(ratings) / float(n_users * n_books), 3)
print ('The sparsity level of Goodbooks-10k dataset is ' +  str(sparsity * 100) + '%')

from scipy.sparse.linalg import svds
U, sigma, Vt = svds(Ratings_demeaned, k = 50)

sigma = np.diag(sigma)
sigma

# Import libraries from Surprise package
from surprise import Reader, Dataset, SVD, accuracy
from surprise.model_selection import cross_validate,KFold

# Load Reader library
reader = Reader()

# Load ratings dataset with Dataset library
data = Dataset.load_from_df(ratings[['user_id', 'book_id', 'rating']], reader)

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

    predictions

    ratings[ratings['user_id'] == 1310]

    svd.predict(1310,61)