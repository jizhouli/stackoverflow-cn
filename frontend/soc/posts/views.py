# calculate ceiling division
from __future__ import division # a/b is float division, 3/2=1.5, 3//2=1
from math import ceil

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect

from posts.models import Posts, Posts1, Posts2, Posts3, Users, MetaTag

# add counter to template script
import itertools

def _post_router(id):
    id = int(id)
    if id < 5885814:
        return Posts
    elif id < 11705308:
        return Posts1
    elif id < 17537164:
        return Posts2
    else:
        return Posts3

### dev interface

def bootstrap(request):
    return render_to_response('bootstrap.html', {})

def bootstrap2(request):
    return render_to_response('bootstrap2.html', {})

def rawsearch(request):
    errors = []
    size = request.GET.get('size', 100)
    query = request.GET.get('query', '')
    if not query:
        errors.append('please enter query word, e.g. "?query=python"')
    else:
        posts = Posts.objects.filter(title__icontains=query)[:size]
        return render_to_response('raw_search.html', {'posts': posts, 'query': query})
    return render_to_response('raw_search_form.html', {'errors': errors})

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

# url map
# ^wiki/    wiki_index.html
# ^wiki/(.+)/   wiki.html
def wiki(request, param='index'):
    if param == "index":
        # REDIRECT search request to restful url
        # "/wiki/?search=java" to "/wiki/java/"
        submit_keyword = request.GET.get('search', '')
        if submit_keyword:
            return HttpResponseRedirect("%s%s/" % (request.path_info, submit_keyword))

        page = request.GET.get('page', '1')
        page = _validate_page(page)
        page_size = request.GET.get('page_size', '48')
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
        cols_width = 4 # must be devided exactily by 12 according to bootstrap Grid System
        cols = []
        cols_matrix = []
        for idx,col in enumerate(tag_list):
            if idx % cols_width == 0:
                if len(cols) > 0: cols_matrix.append(cols)
                cols = []
            cols.append(col)
        if len(cols) > 0:
            cols_matrix.append(cols)

        # get iterator
        iterator=itertools.count()

        # show tag list page
        return render_to_response('wiki_index.html', 
                {
                    'cols_matrix': cols_matrix, 
                    'cols_width': cols_width,
                    'iterator': iterator,
                    'pagination': pagination,
                })

    # show tag search result page
    try:
        tag = MetaTag.objects.get(name=param)
        return render_to_response('wiki.html', {'tag': tag})
    except MetaTag.DoesNotExist:
        # /wiki/404/ -> ['', 'wiki', '404', '']
        # /wiki/aaa/bbb -> /wiki/aaa -> /wiki
        path_split = request.path_info.split('/')
        wiki_index_path = '/'.join(path_split[:len(path_split)-2])
        return HttpResponseRedirect(wiki_index_path)
    except Exception, e:
        return render_to_response('404.html', {'request':request})

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

# url map
# ^questions/tagged/    questions_tagged_index.html
# ^questions/tagged/(.+)/
def tagged(request, param = "index"):
    if param == "index":
        # REDIRECT search request to restful url
        # "/questions/tagged/?search=java" to "/questions/tagged/java/"
        submit_keyword = request.GET.get('search', '')
        if submit_keyword:
            return HttpResponseRedirect("%s%s/" % (request.path_info, submit_keyword))

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
        return render_to_response('questions_tagged_index.html', 
                {
                    'tag_list': tag_list, 
                    'iterator': iterator,
                    'pagination': pagination,
                })

    # show tag search result page
    page = request.GET.get('page', '1')
    page = _validate_page(page)
    page_size = request.GET.get('page_size', '50')
    page_size = _validate_page(page_size)

    post_max = Posts.objects.filter(tags__icontains=param).count()
    # fix bug: 此网页包含重定向循环（ERR_TOO_MANY_REDIRECTS）
    if post_max < 1:
        return render_to_response('404.html', {'request':request})

    page_max = _divide_ceiling(post_max, page_size)
    pagination = _pagination(page_max, page, page_size)
    # REDIRCT exceeding page number to last page
    if page > page_max:
        return HttpResponseRedirect("%s?page=%s" % (request.path_info, page_max))

    offset_begin = (page-1)*page_size
    offset_end = offset_begin + page_size

    try:
        #TODO get questions belong to a tag, then list them
        questions = Posts.objects.filter(tags__icontains=param)[offset_begin:offset_end]
        for i in range(len(questions)):
            tags_str = questions[i].tags
            questions[i].tags = tags_str[1:len(tags_str)-1].split('><')
        return render_to_response('questions_tagged.html', 
                {
                    'posts': questions, 
                    'query': param,
                    'pagination': pagination,
                })
    except Posts.DoesNotExist:
        return render_to_response('404.html', {'request':request})

### Q&A

# url map
# ^questions/
# ^questions/(\d+)/ questions.html
def questions(request, param='index'):
    if param == 'index':
        return HttpResponse('question index page placeholder!')

    try:
        question = _post_router(id=param).objects.get(id=param)
    except Posts.DoesNotExist:
        return render_to_response('404.html', {'request':request})

    
    try:
        author = Users.objects.get(id=question.owneruserid)
    except Users.DoesNotExist, e:
        author = Users.objects.get(id=1)

    if len(question.tags) > 2:
        question.tags = question.tags[1:len(question.tags)-1].split('><')

    aa_id = question.acceptedanswerid
    answer = {}

    if not aa_id:
        return render_to_response('404.html', {'request':request})

    answer = _post_router(id=aa_id).objects.get(id=aa_id)
    answerer = Users.objects.get(id=answer.owneruserid)

    return render_to_response('questions.html',
            {
                'question': question, 
                'answer': answer, 
                'author': author,
                'answerer': answerer,
            })

