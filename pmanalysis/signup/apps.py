from django.apps import AppConfig
from django.contrib import admin
from .models import UserFiles, Study

admin.site.register(UserFiles)
admin.site.register(Study)

class SignupConfig(AppConfig):
    name = 'signup'
