from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal', {
            'fields': ('first_name', 'last_name', 'email', 'postal', 'address')
        }),
        ('Permission', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Date', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Other', {
            'fields': ('money',)
        })
    )

admin.site.register(MyUser, MyUserAdmin)