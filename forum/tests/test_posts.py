from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from forum.models import Post


def create_post(client):
    url = reverse('post_create')
    data = {
        'subject': 'What pill should I take?',
        'detail': 'I want to take the red one...',
    }
    return client.post(url, data=data)


class PostTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'john',
            'email': 'johndoe@example.com',
            'password': '1234',
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_post_create_unauthorized(self):
        response = create_post(self.client)
        self.assertRedirects(
            response, '{login_url}?next={url}'.format(login_url=self.login_url,
                                                      url=reverse('post_create'))
        )
        self.assertEquals(Post.objects.count(), 0)

    def test_post_create(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        response = create_post(self.client)

        self.assertEquals(Post.objects.count(), 1)

        post = Post.objects.first()
        self.assertEquals(post.author, self.user)
        redirect_url = reverse('post_read', kwargs={'post_pk': post.pk})
        self.assertRedirects(response, expected_url=redirect_url)

    def test_post_update(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        # create a post
        create_post(self.client)
        post = Post.objects.first()

        url = reverse('post_update', kwargs={'post_pk': post.pk})
        data = {
            'subject': 'I took the red one!',
            'detail': 'I want to take the red one...',
        }
        response = self.client.post(url, data=data)
        post.refresh_from_db()
        self.assertEquals(post.subject, data['subject'])

        redirect_url = reverse('post_read', kwargs={'post_pk': post.pk})
        self.assertRedirects(response, expected_url=redirect_url)

    def test_post_delete(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        # create a post
        create_post(self.client)
        post = Post.objects.first()

        url = reverse('post_delete', kwargs={'post_pk': post.pk})
        response = self.client.post(url)
        self.assertEquals(Post.objects.count(), 0)

        redirect_url = reverse('posts_list')
        self.assertRedirects(response, expected_url=redirect_url)
