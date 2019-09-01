# Django Visitors App
This is a test django 2.2 application with generic auth, gravatar. It logs visitors of website.

You can view a working version of this app
[here](https://visitapp.herokuapp.com).

## Features

-Django 2.0+
-django-avatar

## Building localy

clone repository to your directory
```powershell
git clone https://github.com/Rokfordchez/visitors.git
```
It is best to use the python `virtualenv` tool to build locally:

powershell
```powershell
cd ../
virtualenv -p python .
source/activate.ps1
pip install -r requirements.txt
cd [your directory]
python manage.py runserver
```
## Description

App shows visitors of website, log ip and time of visit. User can auth and then update profile.
Avatars get from gravatar by email. Localy can download own avatar. But Heroku have readonly file system.

## Contacts
telegram @originalov
