"""visitors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib import admin
from vlist.views import index, register, edit_profile, view_profile, change_password
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='home'),
                  path('index/', index, name="visitors"),
                  path('register/', register, name='register'),
                  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
                  path('edit/', edit_profile, name='edit_profile'),
                  path('avatar/', include('avatar.urls')),
                  path('profile/', view_profile, name='view_profile'),
                  path('password/', change_password, name='password'),
                  path('api/', include('vlist.api.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
