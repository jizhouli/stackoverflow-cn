from django.conf.urls import include, url
from django.contrib import admin

# from posts.views import home
import posts # easy to read, but have to add 'import views' into __init__.py of posts directory to expose outside.

urlpatterns = [
    # Examples:
    # url(r'^$', 'soc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ### developing interface ###
    url(r'^bootstrap/', posts.views.bootstrap),
    url(r'^search/', posts.views.search),
    url(r'^admin/', include(admin.site.urls)),




    ### public interface ###

    # main page 
    url(r'^$', posts.views.index), #home),
    url(r'^index/', posts.views.index),

    # Q&A category
    url(r'^questions/$', posts.views.questions), # list page
    url(r'^questions/(\d+)/$', posts.views.questions), # detail page

    # tag questions category
    url(r'^questions/tagged/$', posts.views.tagged), # list page
    url(r'^questions/tagged/(.+)/$', posts.views.tagged), #detail page

    # tag wiki category
    url(r'^wiki/$', posts.views.wiki), # list page
    url(r'^wiki/(.+)/$', posts.views.wiki), #detail page

]
