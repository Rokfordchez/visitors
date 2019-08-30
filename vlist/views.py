from django.shortcuts import render, redirect
from .models import UList
from django.contrib import messages
from .forms import UserRegisterForm
from django.template import Context
from django.db.models import F
from django.contrib.auth.models import User
from avatar.templatetags.avatar_tags import avatar_url
from ipware import get_client_ip


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
    ip, is_routable = get_client_ip(request)
    if request.user.is_authenticated == True:
        visit = UList(visitor=user, user=user, data=str(ip), image=str(avatar_url(user)))
    else:
        visit = UList(visitor=user, data=str(ip), image='https://www.gravatar.com/avatar/d41d8cd98f00b204e9800998ecf8427e/?s=80')
    visit.save()
    obj = UList.objects.all()
    return render(request, "index.html", {"UList": obj,"counter": visit_num})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)



