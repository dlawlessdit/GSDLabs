from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, board_topics
from .models import Board

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
		
		
class BoardTopicsTests(TestCase):
#Setup an object to represent one of the boards 
    def setUp(self):
        Board.objects.create(name='GSD', description='GSD Board')
#Testing if Django is returning a status code 200 (success) for an existing Board.
    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
#testing if Django is returning a status code 404 (page not found) for a Board that doesn’t exist in the database.
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
#testing if Django is using the correct view function to render the topics.
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)
		
	def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))


		
		
class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='GSD', description='GSD board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
		self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
		
class NewTopicTests(TestCase):
#setUp: creates a Board instance to be used during the tests
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
#test_new_topic_view_success_status_code: check if the request to the view is successful
    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
#test_new_topic_view_not_found_status_code: check if the view is raising a 404 error when the Board does not exist
    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
#test_new_topic_url_resolves_new_topic_view: check if the right view is being used
    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)
#test_new_topic_view_contains_link_back_to_board_topics_view: ensure the navigation back to the list of topics
    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)
		self.assertContains(response, 'href="{0}"'.format(board_topics_url))
