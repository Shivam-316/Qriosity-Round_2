from django.db import models
from django.contrib.auth.models import User
from question.models import Question
# Create your models here.

class Profile(models.Model):
    def num_ques():
        return Question.objects.all().count()
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    ques_id = models.IntegerField(verbose_name='Question At',default=1)
    score = models.IntegerField(default=0)
    attempted = models.IntegerField(default=1)
    total_ques = models.IntegerField(verbose_name='Total Questions',default=num_ques)
    time_taken = models.IntegerField(verbose_name='Total Time',default=0) 
    winner = models.BooleanField(default=False)
    started_quiz = models.BooleanField(default=False,verbose_name="Has Attempted Quiz")

    class Meta:
        ordering=['-score','time_taken']
        
    def __str__(self):
        return f'{self.user.username}\'s Profile'
