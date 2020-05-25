from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
# import rsystem.movierecommd as mrcmd
import json
from .models import Movie
from manage import take
# mrcmd.initialize()
# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_movies(request):
    movies_list = Movie.objects.order_by('id')
    paginator = Paginator(movies_list, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    if page_number==None:
        page_number = 1
    else:
        page_number = int(page_number)
        
    page_obj = paginator.get_page(page_number)
    context_data = list({'id':movie.id, 'name':movie.name, 'rating':movie.rating} for movie in page_obj)
    return JsonResponse({'movies':context_data})


def search(request):
    movie_name = request.GET.get('search_text')
    movies = Movie.objects.filter(Q(name__icontains=movie_name))
    movies = list({'id':movie.id, 'name':movie.name, 'rating':movie.rating} for movie in movies)
    return JsonResponse({'status':'ok', 'movies':movies})

def movie_recommend(request):
    if request.method != "POST":
        return HttpResponse('Only POST request allowed')

    movies = request.POST.get('movies')
    print(movies)
    movies = json.loads(movies)
    # print(request.POST)
    print(movies)
    sol = take(movies)
    print(sol)
    return JsonResponse({'movies':sol})