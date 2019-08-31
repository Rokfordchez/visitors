from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UList
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from avatar.templatetags.avatar_tags import avatar_url
from ipware import get_client_ip
import datetime

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def index(request):
    user = request.user
    visit_num = UList.objects.count()+1
    ip, is_routable = get_client_ip(request)
    try:
        data = str(datetime.datetime.now())+ ', ip:' + str(ip)+f', server_name: {request.META["SERVER_NAME"]}'
    except:
        data = str(datetime.datetime.now())
    if request.user.is_authenticated:
        visit = UList(visitor=user, user=user, data=data, image=str(avatar_url(user)))
    else:
        visit = UList(visitor=user, data=str(ip),
                      image='https://www.gravatar.com/avatar/d41d8cd98f00b204e9800998ecf8427e/?s=80')
    visit.save()

    # update avatars for auth user for old visits
    if request.user.is_authenticated:
        for obj in UList.objects.filter(user=user).exclude(image=str(avatar_url(user))):
            obj.image=str(avatar_url(user))
            obj.save()

    obj = UList.objects.all()
    return render(request, "index.html", {"UList": obj,"counter": visit_num})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'edit_profile.html', {'form': form})

@login_required
def view_profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('view_profile'))
        else:
            return redirect(reverse('password'))
    else:
        form = PasswordChangeForm(user=request.user)

        return render(request, 'password.html', {'form': form})




