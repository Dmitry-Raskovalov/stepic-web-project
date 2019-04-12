from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class QuestionManager(models.Manager):
    def new (self):
        return self.order_by('-id')
    def popular (self):
        return self.order_by('-rating')

class Question(models.Model):
    title    = models.CharField(default='', max_length=255)
    text     = models.TextField(default='')
    added_at = models.DateField(auto_now_add=True)
    rating   = models.IntegerField(default=0)
    author   = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #likes    = models.ManyToManyField(User, related_name='likes_set')
    slug     = models.SlugField(unique=True, null=True)
    objects  = QuestionManager()

    def get_url (self):
        return reverse('qa_question', kwargs={'slug':self.slug})
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text     = models.TextField(default='')
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author   = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)



