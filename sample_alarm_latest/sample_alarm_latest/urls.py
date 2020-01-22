"""sample_alarm_latest URL Configuration

The `urlpatterns` list routes URLs to template. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function template
    1. Add an import:  from my_app import template
    2. Add a URL to urlpatterns:  path('', template.home, name='home')
Class-based template
    1. Add an import:  from other_app.template import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sample_alarm_latest.components import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.test_view, name='test'),
]
