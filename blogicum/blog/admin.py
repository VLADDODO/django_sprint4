from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from .models import Category, Comment, Location, Post

admin.site.empty_value_display = 'Не задано'

admin.site.unregister(Group)

User = get_user_model()

admin.site.unregister(User)  # ← это добавьте


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Настройка раздела Пользователи."""

    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff'
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)