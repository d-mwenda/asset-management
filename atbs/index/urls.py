__author__ = "Derick Mwenda"
"""
These are urls associated with the index app.
Usually, the project urls imports them into its own urls definition for use with the project
"""

from django.urls import path
# atbs
from .views import Dashboard, About

urlpatterns = [
    path('', Dashboard.as_view(), name='u_dashboard'),
    path('about/', About.as_view(), name='u_about'),
]
