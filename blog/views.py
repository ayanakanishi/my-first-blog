from django.shortcuts import render
# the dot before models means current directory, since views.py and models.py are in the same directory. 
# import the name of the model "Post" 
from .models import Post 
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
	# pass "Posts" QuerySet to the template context. Create a variable "posts" for the QuerySet. 
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# in the "render" function, there is one "request" parameter
	# the last parameter in {} is for adding things to be used in the template. 
	return render(request, 'blog/post_list.html', {'posts':posts})
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})