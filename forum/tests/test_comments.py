from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from forum.models import Comment, Post


def create_comment(client, post):
    url = reverse('comment_create', kwargs={'post_pk': post.pk})
    data = {
        'message': 'The red one will take you to the real world.',
    }
    return client.post(url, data=data)


class CommentTest(TestCase):
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
        response = create_comment(self.client, self.post)
        url = reverse('comment_create', kwargs={'post_pk': self.post.pk})
        self.assertRedirects(
            response, '{login_url}?next={url}'.format(login_url=self.login_url, url=url)
        )
        self.assertEquals(Comment.objects.count(), 0)

    def test_comment_create(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        response = create_comment(self.client, self.post)
        comment = Comment.objects.first()
        self.assertEquals(comment.author, self.user)
        self.assertEquals(Comment.objects.count(), 1)

        redirect_url = reverse('post_read', kwargs={'post_pk': self.post.pk})
        self.assertRedirects(response, expected_url=redirect_url)

    def test_comment_update(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        # create a comment
        create_comment(self.client, self.post)
        comment = Comment.objects.first()

        url = reverse('comment_update', kwargs={
            'post_pk': self.post.pk, 'comment_pk': comment.pk
        })
        data = {
            'message': 'The blue is "safer"',
        }
        response = self.client.post(url, data=data)
        comment.refresh_from_db()
        self.assertEquals(comment.message, data['message'])

        redirect_url = reverse('post_read', kwargs={'post_pk': self.post.pk})
        self.assertRedirects(response, expected_url=redirect_url)

    def test_comment_delete(self):
        # login
        self.client.login(username=self.user_data['username'],
                          password=self.user_data['password'])

        # create a comment
        create_comment(self.client, self.post)
        comment = Comment.objects.first()

        url = reverse('comment_delete', kwargs={
            'post_pk': self.post.pk, 'comment_pk': comment.pk
        })
        response = self.client.post(url)
        self.assertEquals(Comment.objects.count(), 0)

        redirect_url = reverse('post_read', kwargs={'post_pk': self.post.pk})
        self.assertRedirects(response, expected_url=redirect_url)
