from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from student_management_app.models import CustomUser

# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser,UserModel)