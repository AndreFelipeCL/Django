# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserAdminCreationForm(UserCreationForm):
    """
    Formulario customizado para criação de novos usuários de acordo com a nova modelagem do usuário do sistema.
    Usando este formulário para o Django Admin.
    UserCreationForm - herdando o formulario do django admin e customizando-o.
    """

    class Meta:
        model = User
        #campos extras para serem apresentados.
        fields = ['username', 'name', 'email']


class UserAdminForm(forms.ModelForm):
    """
    Formulario customizado para atualização de usuários de acordo com a nova modelagem do usuário do sistema.
    Usando este formulário para o Django Admin.
    forms.Modelform - herdando o formulario do django admin e customizando-o.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active']
