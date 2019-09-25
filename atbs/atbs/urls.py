"""atbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import urls as authentication_urls
from django.contrib.auth import views as authentication_views
# atbs imports
from index import urls as index
from assets_register import urls as assets_register
from assets_borrowed import urls as borrowed_assets
from quick_tools import urls as quick_tools

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', authentication_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', authentication_views.LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
    # path('accounts/', include(authentication_urls)),
    path('', include(index)),
    path('asset-management/', include(assets_register)),
    path('quick-tools/', include(quick_tools))
]
