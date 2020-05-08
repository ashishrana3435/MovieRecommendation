import pandas as pd
import numpy as np

def ashish():
    movies_column=['Movie_ID','Title','Category']
    rating_column=['User_ID','Movie_ID','Rating','Timestap']

    movies=pd.read_csv('movie/movies.dat',sep='::',header=None,names=movies_column)
    users=pd.read_csv('movie/users.dat',sep='::',header=None)
    ratings=pd.read_csv('movie/ratings.dat',sep='::',header=None,names=rating_column)

    users.columns=['User_ID','Gender','Age','Occupation','Zip-code']
    data=pd.merge(movies,ratings,on='Movie_ID')

    all_data=pd.merge(data,users,on='User_ID')
    all_data.drop(['Timestap','Zip-code','Occupation'],axis=1).head()
    user_rating=all_data.pivot_table(index='User_ID',columns='Title',values='Rating')

    user_rating=user_rating.dropna(thresh=10,axis=1).fillna(0)
    item_similarity_df=user_rating.corr(method='pearson')

    def get_movie_similarity(movie,rating):
        similar_score=item_similarity_df[movie]*(rating-2.5)
        similar_score=similar_score.sort_values(ascending=False)
        return similar_score
    n=int(input("No. of movies user watched \n"))
    user=[]
    for _ in  range(n):
        x=((input("Movie Name \n")),int(input("Movie rating \n")))
        user.append(x)
    similar_movies=[]
    similar_movies=pd.DataFrame()
    for movie,rating in user:
        similar_movies=similar_movies.append(get_movie_similarity(movie,rating))

    print(similar_movies.sum().sort_values(ascending=False).head())

