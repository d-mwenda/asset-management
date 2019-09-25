from django.urls import path

from .views import GeneratePassword

urlpatterns = [
    path(r'generate-random-password', GeneratePassword.as_view(), name='u_generate_password'),
]