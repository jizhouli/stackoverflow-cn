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
    size = request.GET.get('size', 100)
    query = request.GET.get('query', '')
    if not query:
        errors.append('please enter query word, e.g. "?query=python"')
    else:
        posts = Posts.objects.filter(title__icontains=query)[:size]
        return render_to_response('search.html', {'posts': posts, 'query': query})
    return render_to_response('search_form.html', {'errors': errors})

def tagged(request, param):
    try:
        posts = Posts.objects.filter(tags__icontains=param)[:100]
        return render_to_response('search.html', {'posts': posts, 'query': param})
    except Posts.DoesNotExist:
        return render_to_response('404.html', {})

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
        answerer = Users.objects.get(id=answer.owneruserid)

    return render_to_response('questions.html',
            {
                'question': question, 
                'answer': answer, 
                'author': author,
                'answerer': answerer,
            })

