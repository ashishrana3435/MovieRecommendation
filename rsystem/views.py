from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .movierecommd import ashish
from .models import Movie
# Create your views here.

def index(request):
    movies_list = Movie.objects.all()
    paginator = Paginator(movies_list, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    if page_number==None:
        page_number = 1
    else:
        page_number = int(page_number)
        
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'movies': page_obj, 'prev_page':page_number-1 if page_number>1 else 1 ,'next_page':page_number+1})