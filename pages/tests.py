from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_url(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_home_page_contents(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "home page")

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, "home.html")
