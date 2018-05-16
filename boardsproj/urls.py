
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
#import the views from our boards app
from boards import views

#add a pattern so that if no specific request is made we route to the index method in our views.py of boards

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    url(r'^$', views.index, name='index'),
	url(r'^transport/', views.transport, name='transport'),
	url(r'^about/', views.about, name='about'),
    url(r'^testlang/', views.testlang, name='testlang'),
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    )
