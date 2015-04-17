from django.conf.urls import include, url
from django.contrib import admin

# from posts.views import home
import posts # easy to read, but have to add 'import views' into __init__.py of posts directory to expose outside.

urlpatterns = [
    # Examples:
    # url(r'^$', 'soc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', posts.views.home),
    url(r'^index/', posts.views.index),
    url(r'^search/', posts.views.search),
    url(r'^admin/', include(admin.site.urls)),
]
