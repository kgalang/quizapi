from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=60, verbose_name='title')

class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    question = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices',
    )
    choice = models.CharField(max_length=100)
    is_answer = models.BooleanField(default=False)