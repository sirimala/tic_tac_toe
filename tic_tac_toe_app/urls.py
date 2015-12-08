from django.conf.urls import patterns, include, url
from tic_tac_toe_app.views import *
 
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^game/(?P<id>\d+)/', game),
    url(r'^game/$', game),

    
)