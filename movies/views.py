from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def index(request):
    movies_list = Movie.objects.all().order_by('id')[1:]
    oneMovie = Movie.objects.get(id=1)
    context = {'movies':movies_list,'oneMovie':oneMovie}
    return render(request,'movies/index.html',context)

def movieDetails(request,pk):
    movie_one = Movie.objects.get(id=pk)
    total = movie_one.total_ticket
    ava = movie_one.available_ticket

    if request.method =='POST':
        ava = ava - 1
        if ava <= total:
            movie_one = Movie.objects.filter(id=pk).update(available_ticket=ava)
            return redirect('/')

    context = {'movie':movie_one}
    return render(request,'movies/details.html',context)