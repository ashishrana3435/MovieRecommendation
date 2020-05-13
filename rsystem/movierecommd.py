import pandas as pd
import numpy as np

movies_column=['Movie_ID','Title','Category']
rating_column = ['User_ID', 'Movie_ID', 'Rating', 'Timestap']


def get_movie_similarity(movie,rating,item_similarity_df):
    return (item_similarity_df[movie]*(rating-2.5)).sort_values(ascending=False)

def initialize():
    global movies
    global users
    global ratings
    global user_rating
    global item_similarity_df
    
    movies=pd.read_csv('rsystem/movie/movies.dat',sep='::', header=None, names=movies_column, engine='python')
    users=pd.read_csv('rsystem/movie/users.dat',sep='::', header=None, engine='python')
    ratings=pd.read_csv('rsystem/movie/ratings.dat',sep='::', header=None, names=rating_column, engine='python')
    print('read all files')

    users.columns = ['User_ID', 'Gender', 'Age', 'Occupation', 'Zip-code']

    data=pd.merge(movies,ratings,on='Movie_ID')
    all_data=pd.merge(data,users,on='User_ID')
    print('files merged')

    all_data.drop(['Timestap','Zip-code','Occupation'],axis=1).head()

    user_rating=all_data.pivot_table(index='User_ID',columns='Title',values='Rating')
    print('pivot table')

    user_rating = user_rating.dropna(thresh=10, axis=1).fillna(0)
    print('dropped')

    item_similarity_df = user_rating.corr(method='pearson')
    print('pearson correlation applied')


def take(X):
    n=int(input("No. of movies user watched \n"))
    user=[]

    for _ in  range(n):
        x=((input("Movie Name \n")),int(input("Movie rating \n")))
        user.append(x)

    similar_movies=[]
    similar_movies=pd.DataFrame()

    for movie,rating in user:
        similar_movies.append(get_movie_similarity(movie,rating,item_similarity_df))

    print(similar_movies.sum().sort_values(ascending=False).head())
