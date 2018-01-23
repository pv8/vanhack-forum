from django.conf.urls import url

from forum import views

urlpatterns = [
    url(r'^$', views.posts_list, name='posts_list'),

    # Posts CRUD
    url(r'^post/new/$', views.post_create, name='post_create'),
    url(r'^post/(?P<post_pk>\d+)/$', views.post_read, name='post_read'),
    url(r'^post/(?P<post_pk>\d+)/edit/$', views.post_update, name='post_update'),
    url(r'^post/(?P<post_pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    # Comments CRUD
    url(r'^post/(?P<post_pk>\d+)/comment/new$', views.comment_create, name='comment_create'),
    url(r'^post/(?P<post_pk>\d+)/comment/(?P<comment_pk>\d+)/edit/$', views.comment_update,
        name='comment_update'),
    url(r'^post/(?P<post_pk>\d+)/comment/(?P<comment_pk>\d+)/delete/$', views.comment_delete,
        name='comment_delete'),

    # Categories CRUD
    url(r'^categories/$', views.categories_list, name='categories_list'),
    url(r'^category/new$', views.category_create, name='category_create'),
    url(r'^category/(?P<category_pk>\d+)/edit/$', views.category_update, name='category_update'),
    url(r'^category/(?P<category_pk>\d+)/delete/$', views.category_delete, name='category_delete'),
]
