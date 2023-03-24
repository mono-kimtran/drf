from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Profile
# Register your models here.

User = get_user_model()


class UserAdminConfig(UserAdmin):
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'is_staff', 'is_active',)
    list_editable = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name',)},),
        ('Permission', {'fields': ('is_staff', 'is_active', 'groups')},),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)
        }),
    )


class ProfileAdminConfig(admin.ModelAdmin):
    model = Profile
    ordering = ('-date_created',)
    list_display = ('user', 'phone',)


admin.site.register(User, UserAdminConfig)
admin.site.register(Profile, ProfileAdminConfig)
