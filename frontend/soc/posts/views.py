# calculate ceiling division
from __future__ import division # a/b is float division, 3/2=1.5, 3//2=1
from math import ceil

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect

from posts.models import Posts, Users, MetaTag

# add counter to template script
import itertools

### dev interface

def bootstrap(request):
    return render_to_response('bootstrap.html', {})

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

### exceptional status code 

def handler404(request):
    response = render_to_response('404.html', {},
            context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
            context_instance=RequestContext(request))
    response.status_code = 500
    return response

### main page

def home(request):
    return HttpResponse('hello home!')

def index(request):
    return render_to_response('index.html', {})

### tag wiki

def wiki(request, param='index'):
    return HttpResponse('wiki page placeholder!')

### tag questions

def _validate_page(page):
    try:
        page = int(float(page))
    except Exception, e:
        page = 0

    return page if page>1 else 1

# calculate ceiling division
def _divide_ceiling(dividend, divisor):
    if not divisor:
        return 0

    ceiling_quotients = int(ceil(dividend/divisor))
    return ceiling_quotients

def _pagination(page_max, page, page_size, page_min=1):
    page_up = page_max if page+1 > page_max else page+1
    page_down = page_min if page-1 < page_min else page-1
    pagination = {
            'page_up': {
                'enable': False if page==page_max else True,
                'value': page_up,
                },
            'page_down': {
                'enable': False if page==page_min else True,
                'value': page_down,
                },
            'page_size': page_size,
            }
    return pagination

def tagged(request, param = "index"):
    if param == "index":
        # REDIRECT search request to restful url
        # "/questions/tagged/?search=java" to "/questions/tagged/java/"
        submit_keyword = request.GET.get('search', '')
        if submit_keyword:
            return HttpResponseRedirect("%s%s" % (request.path_info, submit_keyword))

        page = request.GET.get('page', '1')
        page = _validate_page(page)
        page_size = request.GET.get('page_size', '50')
        page_size = _validate_page(page_size)

        # get pagination
        tag_max = MetaTag.objects.count()
        page_max = _divide_ceiling(tag_max, page_size)
        pagination = _pagination(page_max, page, page_size)

        # REDIRCT exceeding page number to last page
        if page > page_max:
            return HttpResponseRedirect("%s?page=%s" % (request.path_info, page_max))

        offset_begin = (page-1)*page_size
        offset_end = offset_begin + page_size
        
        # get tag list
        tag_list = MetaTag.objects.all().order_by('-sum')[offset_begin:offset_end]

        # get iterator
        iterator=itertools.count()

        # show tag list page
        return render_to_response('tag_list.html', 
                {
                    'tag_list': tag_list, 
                    'iterator': iterator,
                    'pagination': pagination,
                })

    # show tag search result page
    try:
        posts = Posts.objects.filter(tags__icontains=param)[:100]
        return render_to_response('search.html', {'posts': posts, 'query': param})
    except Posts.DoesNotExist:
        return render_to_response('404.html', {})

### Q&A

def questions(request, param='index'):
    if param == 'index':
        return HttpResponse('question index page placeholder!')

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

