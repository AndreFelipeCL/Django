# coding=utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserAdminCreationForm, UserAdminForm

class UserAdmin(BaseUserAdmin):
    list_display = ['name', 'username', 'email', 'is_active', 'is_staff', 'data_joined']
    search_fields = ['name', 'username', 'email']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    form = UserAdminForm
    add_fieldsets = (
        ('Novo Usuário - Dados Obrigatórios', {
            'fields': ('name', 'username', 'email', 'password1', 'password2')
        }),
    )
    fieldsets = (
        ('Identificação', {
            'fields': ('username', 'email')
        }),

        ('Informações Básicas', {
            'fields': ('name', 'last_login')
        }),

        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )
    add_form = UserAdminCreationForm

admin.site.register(User, UserAdmin)
