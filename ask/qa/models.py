from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new (self):
        return self.order_by('-id')
    def popular (self):
        return self.order_by('-rating')

class Question(models.Model):
    title    = models.CharField(default='', max_length=255)
    text     = models.TextField(default='')
    added_at = models.DateField(blank=True)
    rating   = models.IntegerField(default=0)
    author   = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes    = models.ManyToManyField(User, related_name='likes_qst')
    objects  = QuestionManager()

class Answer(models.Model):
    text     = models.TextField(default='')
    added_at = models.DateField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author   = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)



