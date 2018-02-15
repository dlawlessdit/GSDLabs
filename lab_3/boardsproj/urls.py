
from django.conf.urls import url
from django.contrib import admin

#import the views from our boards app
from boards import views

#add a pattern so that if no specific request is made we route to the home method in our views.py of boards

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]