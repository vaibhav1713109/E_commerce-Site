from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Movie, MovieImage
import re


def index(request):
    try:
        movies=Movie.objects.all()
        #print(movies,1)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context={'movies':movies, 'data':[1,2,3]}
    return render(request, 'i_Movie/index.html', context)    
    #return HttpResponse("Hello, world. You're at the polls index.")

def Details(request,pk):
    try:
        movie=get_object_or_404(Movie, id=pk)
        movies=Movie.objects.filter(id=pk)
        m=Movie.objects.all()
        screenshots=MovieImage.objects.filter(screenshot=movie)
        #print(movie)
        #print(movies,1)
        #print(screenshots)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context={'screenshots':screenshots,'movies':movies,"m":m}
    return render(request, 'i_Movie/details.html', context) 

def searchmatch(query,item):
    if query in (item.name.lower() or item.description.lower() or item.category.lower()):
        return True
    else:
        return False    

def search(request):
    #return HttpResponse('this is search page')
    queryy=request.GET.get('search')
    #print(queryy)
    query=queryy.lower()
    movie_list=Movie.objects.all()
    Movies=[]
    for item in movie_list:
        if searchmatch(query,item):
            Movies.append(item)

    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0 or len(query)<=4:
        prams={'msg':"Please make sure to enter relevent search query"}
    return render(request,'i_Movie/search.html',prams)

def Action(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'action', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Action.html',prams)

def Adventure(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'adventure', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Adventure.html',prams)

def Comedy(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'comedy', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Comedy.html',prams)

def Animated(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'animated', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Animated.html',prams)

def Crime(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'crime', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Crime.html',prams)

def Horror(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'horror', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Horror.html',prams)

def Fantasy(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'fantasy', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Fantasy.html',prams)

def Sci_Fi(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'sci-fi', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Sci-Fi.html',prams)

def Romentic(request):
    movies=Movie.objects.all()
    Movies=[]
    for cat in movies:
        categs=cat.category.lower()
        match = re.search(r'romentic', categs)
        if match:
            #print('found')
            Movies.append(cat)
        else:
            #print('not found')
            pass
    prams={"Movies":Movies,"msg":""}
    if len(Movies)==0:
        prams={'msg':"Please make sure to enter relevent search query"} 
    return render(request,'i_Movie/Romentic.html',prams)

