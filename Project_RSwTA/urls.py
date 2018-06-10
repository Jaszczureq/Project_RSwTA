"""Project_RSwTA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin, auth
from django.urls import include
from django.views.generic import TemplateView
from polls import views

app_name = ''
urlpatterns = [
    url('', TemplateView.as_view(template_name="index.html"), name='index'),
    url('polls/', include('polls.urls')),
    url('admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
	url('accounts/signup', views.signup, name='signup'),
	
]
