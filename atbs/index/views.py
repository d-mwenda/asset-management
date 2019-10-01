from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy


class Dashboard(TemplateView):
    template_name = 'index/dashboard.html'

    def get(self, request, *args, **kwargs):
        response = redirect(reverse_lazy('login'))
        return response


class About(TemplateView):
    pass
