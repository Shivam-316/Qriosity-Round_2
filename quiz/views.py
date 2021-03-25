from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from question.models import Question
from quiz.forms import AnswerForm,TimeForm
from userProfile.models import Profile
from django.http import JsonResponse
import json
from datetime import datetime,timedelta
from django.contrib.auth.decorators import login_required
import time
import pytz

#------------ Global Constants -----------#
IST = pytz.timezone('Asia/Kolkata')
starttime = IST.localize(datetime(2021,3,25,21,5,0,0))
endtime = IST.localize(datetime(2021,3,25,21,7,0,0))
#-----------------------------------------#

# Create your views here.
@login_required
def checkAns(request):
    if request.is_ajax() and request.method=="POST":
        profile = request.user.profile
        form=AnswerForm(request.POST)
        if form.is_valid():
            question_obj = get_question_obj(profile)
            tmp_answer = form.cleaned_data.get('answer')
            ori_answer = question_obj.ans
            if tmp_answer == ori_answer:
                profile.score+=question_obj.correct_score
                profile.save()
                data = {'isCorrect':True}
                return JsonResponse(data)
            else:
                profile.score-=question_obj.wrong_score
                profile.save()
                data = {'isCorrect':False}
                return JsonResponse(data)

@login_required
def quizView(request):
    profile = request.user.profile
    if request.is_ajax() and request.method=="POST":
        form = TimeForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data.get('time')
            profile.time_taken += time
            profile.save()
        if profile.attempted >= profile.total_ques:
            profile.winner=True
            profile.save()
            data = {'winner':True}
            return JsonResponse(data)
        else:
            questionObject = get_next_question(profile)
            data = get_context_obj(questionObject,profile)
            return JsonResponse(data)
    elif request.method == "GET":
        if profile.started_quiz == False and starttime < datetime.now(tz=IST) < endtime:
            profile.started_quiz = True
            profile.save()
            questionObject = get_question_obj(profile)
            data = get_context_obj(questionObject,profile)
            return render(request,'quiz.html',{"data":data,"form":AnswerForm,'time':TimeForm,'winner':profile.winner})
        else:
            return redirect(reverse_lazy('leaderboard'))



@login_required
def get_question_obj(profile):
    if(profile.attempted <= profile.total_ques):
        return Question.objects.get(id=profile.ques_id)

@login_required
def get_next_question(profile):
    while True:
        if profile.ques_id <= Question.objects.last().id:
            profile.ques_id+=1
            profile.save()
        try:
            quesObj=Question.objects.get(pk=profile.ques_id)
        except ObjectDoesNotExist:
            continue
        else:
            break
    profile.attempted+=1
    profile.save()
    return quesObj

def get_context_obj(questionObject,profile):
    return {
            'question':questionObject.ques,
            'A':questionObject.choice1,
            'B':questionObject.choice2,
            'C':questionObject.choice3,
            'D':questionObject.choice4,
            'total_ques': profile.total_ques,
            'attempted':profile.attempted,
            'progress':(profile.attempted/profile.total_ques)*100,
            'timer':questionObject.timer,
            'winner':profile.winner
        }


def leaderboardView(request):
    profiles = Profile.objects.filter(user__is_staff=False)
    leaderboard_data = []
    for profile in profiles:
        leaderboard_data.append({'user':profile.user.username,'score':profile.score,'time':profile.time_taken})
    data = {'profiles':leaderboard_data}
    return render(request,'leaderboard.html',data)