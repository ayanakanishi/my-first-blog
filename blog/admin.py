from django.contrib import admin
from .models import Post

# import the Post model so that it's visible on the admin page. 
admin.site.register(Post)

