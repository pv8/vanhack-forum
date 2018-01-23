from django.test import TestCase
from django.urls import reverse


class HomeTest(TestCase):

    def test_home_redirect(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertRedirects(response, '/forum/')

    def test_home_forum(self):
        url = reverse('posts_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'href="{0}"'.format(url))
