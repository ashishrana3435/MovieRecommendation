import pandas as pd
import numpy as np
# def get_movie_similarity(movie,rating):
# 	similar_score=item_similarity_df[movie]*(rating-2.5)
# 	similar_score=similar_score.sort_values(ascending=False)
# 	return similar_score

def get_movie_similarity(movie,rating,item_similarity_df):
	return (item_similarity_df[movie]*(rating-2.5)).sort_values(ascending=False)

def initialize():
	global movies
	global users
	global ratings
	global user_rating
	global item_similarity_df
	global movies_column
	global rating_column

	movies_column=['Movie_ID','Title','Category']
	rating_column = ['User_ID', 'Movie_ID', 'Rating', 'Timestap']

	print('reading files .....')
	movies=pd.read_csv('rsystem/movie/movies.dat',sep='::', header=None, names=movies_column, engine='python')
	users=pd.read_csv('rsystem/movie/users.dat',sep='::', header=None, engine='python')
	ratings=pd.read_csv('rsystem/movie/ratings.dat',sep='::', header=None, names=rating_column, engine='python')
	print('read all files')

	users.columns = ['User_ID', 'Gender', 'Age', 'Occupation', 'Zip-code']

	print('merging files........')
	data=pd.merge(movies,ratings,on='Movie_ID')
	all_data=pd.merge(data,users,on='User_ID')
	print('files merged')

	all_data.drop(['Timestap','Zip-code','Occupation'],axis=1).head()

	print('pivoting table .......')
	user_rating = all_data.pivot_table(index='User_ID',columns='Title',values='Rating')
	print('pivot table')


	print('dropping ......')
	user_rating = user_rating.dropna(thresh=10, axis=1).fillna(0)
	print('dropped')
	
	print('applying pearson correlation on dataset ............')
	item_similarity_df = user_rating.corr(method='pearson')
	# item_similarity_df = []
	print('pearson correlation applied')


def take(movies: [map]):
	similar_movies = pd.DataFrame()
	# return movies
	for movie in movies:
		similar_movies = similar_movies.append(get_movie_similarity(movie['movie'], movie['rating'], item_similarity_df))
	return similar_movies.sum().sort_values(ascending=False).head().to_dict()    