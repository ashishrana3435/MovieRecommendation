#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from rsystem import movierecommd as mcrmd

print('__name__', __name__)

def take(movies: [map]):
    return mcrmd.take(movies)
	# similar_movies = pd.DataFrame()
	# # return movies
	# for movie in movies:
	# 	similar_movies = similar_movies.append(get_movie_similarity(movie['movie'], movie['rating'], item_similarity_df))

	# return similar_movies.sum().sort_values(ascending=False).head().to_dict()    

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecomendationSystem.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    mcrmd.initialize()
    main()
