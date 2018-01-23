from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from forum.models import Category, Post


def create_category(client):
    url = reverse('category_create')
    data = {
        'name': 'matrix',
        'description': 'Matrix related stuff',
    }
    return client.post(url, data=data)


class CategoryTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'john',
            'email': 'johndoe@example.com',
            'password': '1234',
        }
        self.user = User.objects.create_user(**self.user_data)
        self.post = Post.objects.create(
            subject='What pill should I take?', detail='I want to take the red one...',
            author=self.user
        )

    def test_comment_create_unauthorized(self):
        response = create_category(self.client)
        url = reverse('category_create')
        self.assertRedirects(
            response, '{login_url}?next={url}'.format(login_url=self.login_url, url=url)
        )
        self.assertEquals(Category.objects.count(), 0)

    def test_comment_create(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        response = create_category(self.client)

        self.assertEquals(Category.objects.count(), 1)

        redirect_url = reverse('categories_list')
        self.assertRedirects(response, expected_url=redirect_url)

    def test_comment_update(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        # create a category
        create_category(self.client)
        category = Category.objects.first()

        url = reverse('category_update', kwargs={'category_pk': category.pk})
        data = {
            'name': 'world',
            'description': 'There is no matrix',
        }
        response = self.client.post(url, data=data)
        category.refresh_from_db()
        self.assertEquals(category.name, data['name'])
        self.assertEquals(category.description, data['description'])

        redirect_url = reverse('categories_list')
        self.assertRedirects(response, expected_url=redirect_url)

    def test_category_delete(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        # create a category
        create_category(self.client)
        category = Category.objects.first()

        url = reverse('category_delete', kwargs={'category_pk': category.pk})
        response = self.client.post(url)
        self.assertEquals(Category.objects.count(), 0)

        redirect_url = reverse('categories_list')
        self.assertRedirects(response, expected_url=redirect_url)
