"""tic_tac_toe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tic_tac_toe_app.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('tic_tac_toe_app.urls')),
    url(r'^game/', include('tic_tac_toe_app.urls')),
    url(r'^home/', 'tic_tac_toe_app.views.home'),
    url(r'^logout/', 'tic_tac_toe_app.views.logout', logout_page),
    url(r'^register/', 'tic_tac_toe_app.views.register'),
    url(r'^mygame/', 'tic_tac_toe_app.views.mygame'),
]
