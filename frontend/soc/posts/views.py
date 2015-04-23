from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

from posts.models import Posts, Users

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

def tagged(request, param):
    return HttpResponse('hello %s' % (param))

def questions(request, param):
    try:
        question = Posts.objects.get(id=param)
    except Posts.DoesNotExist:
        return render_to_response('404.html', {})

    author = Users.objects.get(id=question.owneruserid)
    if len(question.tags) > 2:
        question.tags = question.tags[1:len(question.tags)-1].split('><')

    aa_id = question.acceptedanswerid
    answer = {}
    if aa_id:
        answer = Posts.objects.get(id=aa_id)
    return render_to_response('questions.html',
            {'question': question, 'answer': answer, 'author': author})

