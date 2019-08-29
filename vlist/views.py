from django.shortcuts import render, redirect
from .models import UList
from django.contrib import messages
from .forms import UserRegisterForm
from django.template import Context
from django.db.models import F
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def index(request):
    user = request.user
    visit_num = UList.objects.count()+1
    if request.user.is_authenticated == True:
        visit = UList(visitor=user, user=user, data=str(request.GET.items()))
    else:
        visit = UList(visitor=user, data=str(request.GET.items()))
    visit.save()
    list = UList.objects.all()
    return render(request, "index.html", {"UList": list,"counter": visit_num})




