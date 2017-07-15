# coding=utf-8

from core.forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()


# class LoginView(TemplateView):
#     template_name = 'login.html'
#
# login = LoginView.as_view()



def contact(request):
    success = False
    # Entede-se aqui como sendo uma operação ternária em Python. Caso a avaliação
    # boolena do primeira termo serja False, não existente, ele envia um None.
    # Se estamo passando um None, o DJango entende que nosso formulario nao está
    # preenchido e sem validar, o que não mostra mensagem de erro. Seria como uma
    # nova instanciação do mesmo: form = ContactForm()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True

    context = {
        'title': 'Fale Conosco',
        'form': form,
        'success': success,
    }
    return render(request, 'contact.html', context)
