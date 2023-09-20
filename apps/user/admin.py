from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from django.contrib.admin import ModelAdmin
from apps.user.models import User


# Register your models here.
class CustomUser(UserAdmin):
    pass


admin.site.register(User, CustomUser)
