from django.db import models

# Create your models here.
class Question(models.Model):
    ques = models.TextField(verbose_name="Question ")
    choice1 = models.CharField(max_length=200,verbose_name="A ")
    choice2 = models.CharField(max_length=200,verbose_name="B ")
    choice3 = models.CharField(max_length=200,verbose_name="C ")
    choice4 = models.CharField(max_length=200,verbose_name="D ")
    ans = models.CharField(max_length=200,verbose_name="Answer ")
    timer = models.PositiveIntegerField(verbose_name="Time(s) ",default=15)
    correct_score = models.PositiveIntegerField(verbose_name="Score For Corrent Answer ",default=5)
    wrong_score = models.PositiveIntegerField(verbose_name="Neg. Score For Wrong Answer ",default=3)

    def __str__(self):
        return self.ques[:50]
