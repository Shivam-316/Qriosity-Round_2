from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Profile
def signUpView(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect(reverse('instructions'))
        else:
            return render(request,'registration/signup.html',{'form':form})
    else:
        form=SignupForm()
        return render(request,'registration/signup.html',{'form':form})
