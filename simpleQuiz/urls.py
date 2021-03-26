"""simpleQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quiz.views import quizView,checkAns,leaderboardView,countDownView
from django.contrib.auth.views import LoginView,LogoutView
from userProfile.views import signUpView
from django.views.generic import TemplateView 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(template_name='registration/login.html'),name="login"),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'),name="logout"),
    path('signup/',signUpView,name="signup"),
    path('check/',checkAns,name='checkAns'),
    path('leaderboard/',leaderboardView,name='leaderboard'),
    path('countdown/',countDownView,name='countdown'),
    path('quiz/',quizView,name='quiz'),
    path('instructions/',TemplateView.as_view(template_name='instructions.html'),name='instructions'),
    path('',TemplateView.as_view(template_name='home.html'),name='home')
]
