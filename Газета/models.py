import datetime
from django.db import models

from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=40, unique= True)
    description = models.TextField()

    def _str_(self):
        return self.name

    class Meta:
            verbose_name = 'Категория'
            verbose_name_plural = 'Категории'

class Author(models.Model):
    user = models.OneToOneField(User,on_delate=models.CASCADE)

    def _str_(self):
        return self.user

    class Meta:
            verbose_name = 'Автор'
            verbose_name_plural = 'Авторы'

class Post(models.Model):
    post_title = models.CharField(' Название поста', max_length =300)
    post_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def _str_(self):
        return self.post_title
    
    def was_published_resently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))
    

    class Meta:
            verbose_name = 'Пост'
            verbose_name_plural = 'Посты'

class PostCategory(models.Model):

     def _str_(self):
        return self.name

     class Meta:
            verbose_name = 'Автор'
            verbose_name_plural = 'Авторы'

class Comment(model.Model):
    article = models.ForeingnKey(Post, on_delete = models.CASCADE)
    autor_name = models.CharField('имя автора', max_length = 60)
    comment_text = models.CharField('текст коментария', max_length = 300)
   
    def _str_(self):
        return self. author_name

    class Meta:
            verbose_name = 'Коментарий'
            verbose_name_plural = 'Коментарии'



