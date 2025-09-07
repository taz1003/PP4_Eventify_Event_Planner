# Create your tests here.
from django.test import TestCase


class AboutPageTests(TestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'about/about.html')
