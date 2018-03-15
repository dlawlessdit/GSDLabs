
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

#import the views from our boards app
from boards import views

#add a pattern so that if no specific request is made we route to the home method in our views.py of boards


urlpatterns=[]
urlpatterns += i18n_patterns(
	url(r'^$', views.home, name='home'),
	url(r'^testlang/', views.testlang, name='testlang'),
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    )