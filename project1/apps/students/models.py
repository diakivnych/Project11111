from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField('Имя', max_length = 20)
    last_name = models.CharField('Фамилия', max_length = 20)
    age = models.IntegerField('Возраст')
    job = models.CharField('Робота', max_length = 20)
    hobby = models.TextField('Хобби')

    def __str__(self):
    	return self.last_name

class Comment(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 20)
    comment_text = models.CharField('Текст комментария', max_length = 200)
    pub_date = models.DateTimeField('Дата публикации комментария')

    def __str__(self):
    	return self.author_name