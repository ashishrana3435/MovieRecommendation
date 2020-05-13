from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('get_movies',views.get_movies, name='movies'),
    path('search', views.search, name='search'),
    path('recommend',views.movie_recommend, name='recommend')
]