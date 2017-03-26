# import Django's function url and all of our views from the blog app. 
from django.conf.urls import url
from . import views

# assign a view called post_list to the ^$ URL. 
# regex will match ^ (beginning) followed by $ (end), only empty strings
# if someone enters the website, go to views.post_list
urlpatterns = [
	url(r'^$', views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]