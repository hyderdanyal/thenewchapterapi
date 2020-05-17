from surprise import Reader, Dataset, SVD, accuracy
from surprise.model_selection import cross_validate,KFold
import numpy as np
import pandas as pd
import pickle
from scipy.sparse.linalg import svds

def training():
    ratings = pd.read_csv('dataset/ratings.csv',  usecols=['user_id', 'book_id', 'rating'])
    ratings['user_id'] = ratings['user_id'].apply(str)
    
    n_users = ratings.user_id.unique().shape[0]
    n_books = ratings.book_id.unique().shape[0]
    # print('Number of users = ' + str(n_users) + ' | Number of books = ' + str(n_books))

    Ratings = ratings.pivot(index = 'user_id', columns ='book_id', values = 'rating').fillna(0)
    # Ratings.head()

    R = Ratings.to_numpy()
    user_ratings_mean = np.mean(R, axis = 1)
    Ratings_demeaned = R - user_ratings_mean.reshape(-1, 1)

    sparsity = round(1.0 - len(ratings) / float(n_users * n_books), 3)
    # print ('The sparsity level of MovieLens1M dataset is ' +  str(sparsity * 100) + '%')

    U, sigma, Vt = svds(Ratings_demeaned, k = 50)

    sigma = np.diag(sigma)
    # sigma

    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

    preds = pd.DataFrame(all_user_predicted_ratings, columns = Ratings.columns)
    # preds.head()

    # def recommend_movies(predictions, userID, movies, original_ratings, num_recommendations):
        
    #     # Get and sort the user's predictions
    #     user_row_number = userID - 1 # User ID starts at 1, not 0
    #     sorted_user_predictions = preds.iloc[user_row_number].sort_values(ascending=False) # User ID starts at 1
        
    #     # Get the user's data and merge in the movie information.
    #     user_data = original_ratings[original_ratings.user_id == (userID)]
    #     user_full = (user_data.merge(books, how = 'left', left_on = 'book_id', right_on = 'book_id').
    #                     sort_values(['rating'], ascending=False)
    #                 )

    #     print ('User {0} has already rated {1} movies.'.format(userID, user_full.shape[0]))
    #     print ('Recommending highest {0} predicted ratings movies not already rated.'.format(num_recommendations))
        
    #     # Recommend the highest predicted rating movies that the user hasn't seen yet.
    #     recommendations = (books[~books['book_id'].isin(user_full['book_id'])].
    #         merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left',
    #             left_on = 'book_id',
    #             right_on = 'book_id').
    #         rename(columns = {user_row_number: 'Predictions'}).
    #         sort_values('Predictions', ascending = False).
    #                     iloc[:num_recommendations, :-1]
    #                     )

    #     return user_full, recommendations

    # already_rated, predictions = recommend_movies(preds, 1310, books, ratings, 20)


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
    print('Data Trained Successfully')
    with open('model_pickle','wb') as f:
        pickle.dump(svd,f)
training()        