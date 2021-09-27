"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.shortcuts import render
from django.urls import include, path


def home(request, *args, **kwargs):
    return render(request=request, template_name='index.html')


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('persons/', include('gestionusers.views')),
    path('patients/', include('gestionpatient.views')),
    path('patient/', include('formparent.views')),
    path('patient/', include('formteacher.views')),
    path('messages/', include('chat.views'))
]
