# coding=utf-8

from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import User
from django.core.urlresolvers import reverse_lazy
from .forms import UserAdminCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'

index = IndexView.as_view()


class RegisterView(LoginRequiredMixin, CreateView):
    model = get_user_model()
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/register.html'

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(None, reverse_lazy('index'), None)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return self.handle_no_permission()
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

register = RegisterView.as_view()
