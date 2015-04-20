from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

from posts.models import Posts

def home(request):
    return HttpResponse('hello home!')

def bootstrap(request):
    return render_to_response('bootstrap.html', {})

def index(request):
    return render_to_response('index.html', {})

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters')
        else:
            posts = Posts.objects.filter(title__icontains=q)[:10]
            return render_to_response('search.html',
                    {'posts': posts, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})
