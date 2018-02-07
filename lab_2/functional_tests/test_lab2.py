# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase  
import time
import unittest

class TestLab2(LiveServerTestCase): 
 
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn("A Sample Django App!", self.browser.title)
        time.sleep(5)

    def test_h1_css(self):
        self.browser.get('http://localhost:8000')
        h1 = self.browser.find_element_by_tag_name("h1")
        print (h1.value_of_css_property("color"))
        self.assertEqual(h1.value_of_css_property("color"), 
                         "rgb(255, 192, 203)")
 

if __name__ == '__main__':
    unittest.main(warnings='ignore')