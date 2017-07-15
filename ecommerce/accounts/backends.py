# coding=utf-8

from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from django.contrib.auth import get_user_model

class ModelBackend(BaseModelBackend):
    """docstring for ModelBackend."""

    def authenticate(self, username=None, password=None):
        if not username is None:
            # get_user_model() irá pegar o usuário da nossa aplicação customizado, uma vez que definimos este no settings.py
            # na variavel AUTH_USER_MODEL = 'accounts.User' . Com isso, nosso sistema sobrescreverá o usuário default e
            # fazendo o get_user_model retornar o que precisamos, isto deixa a aplicação mais plugável e não descaracteriza
            # o Django.
            UserModel = get_user_model()
            try:
                user = UserModel.objects.get(email=username)
                if user.check_password(password):
                    return user
            except UserModel.DoesNotExist as e:
                pass
