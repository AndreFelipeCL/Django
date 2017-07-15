# coding=utf-8

import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    """
        Clase customizada para Usuários.
        AbstractBaseUser - Herança base do Django para criar usuário e realizar registros e login da mesma forma.
        PermissionsMixin - Herança do Django para que possamos usar esta modelagem de usuário como Administrador do sistema admin.
    """
    # Atributo do usuario do qual Django usará para as suas regras de negócio
    username = models.CharField(
        'Apelido / Usuário',
        max_length = 200,
        unique = True,
        validators = [
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Informe um nome de usuário válido. '
            'Este valor deve conter apenas letras, números e os caracteres @/./+/-/_ .', 'invalid' )
        ],
        help_text = 'Um nome curto que será usado para identificá-lo de forma única na plataforma')

    # Django utiliza first_name e last_name, aqui estamos usando um atributo só para o nome completo
    name = models.CharField(
        'Nome',
        max_length=100)

    # Determinando que o campor de E-mail seja unico para nossa aplicação, diferentemente do Django.
    email = models.EmailField(
        'E-mail',
        unique = True)

    # Atributo que nos diz se o usuário é um membro da equipe (Administrador)
    is_staff = models.BooleanField(
        'Menbro da Equipe',
        default = False)

    # Atributo que nos diz se o usuário está ativo no sistema
    is_active = models.BooleanField(
        'Ativo',
        default = True)

    # Data de criação do usuário do qual o Django realiza de maneira automática.
    data_joined = models.DateTimeField(
        'Data de Entrada',
        auto_now_add = True)

    # Usado pelo Django para determinar qual Atributo do nosso usuário customizado ele irá trabalhar como Atributo de login e etc.
    USERNAME_FIELD = 'username'
    # Determinar ao Django que os Atributos listados aqui são obrigatórios na criação do usuário
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name', 'is_superuser', 'is_staff', 'is_active']

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
