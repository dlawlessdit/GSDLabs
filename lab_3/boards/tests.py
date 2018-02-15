from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
#we are making use of the resolve function.
#Django uses it to match a requested URL with a list of URLs listed in the urls.py module. 
#This test will make sure the URL /, which is the root URL, is returning the home view.
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)