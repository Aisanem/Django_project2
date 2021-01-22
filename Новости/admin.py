from django.contrib import admin
from news.models import Category
from news.models import Author
from news.models import Post
from news.models.import PostCategory
from news. models.import Comment

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

