import secrets
import string
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# ATBS imports
from .forms import PasswordGeneratorForm


class GeneratePassword(LoginRequiredMixin, FormView):
    template_name = 'quick_tools/generate_password.html'
    form_class = PasswordGeneratorForm
    view_name = "Generate Random Password"
    success_url = reverse_lazy('u_generate_password')
    password = None

    def generate_random_password(self, length=20):
        alphabet = string.ascii_letters + string.digits
        self.password = ''.join(secrets.choice(alphabet) for i in range(length))

    def get_context_data(self, **kwargs):
        ctx = super(GeneratePassword, self).get_context_data()
        ctx['view_name'] = self.view_name
        ctx['password'] = self.password
        return ctx

    def form_valid(self, form):
        self.generate_random_password(length=form.cleaned_data['length'])
        return self.render_to_response(self.get_context_data())

