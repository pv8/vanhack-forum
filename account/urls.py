from django.conf.urls import url
from django.contrib.auth import views as django_auth_views

from account import views


urlpatterns = [
    # auth
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', django_auth_views.LoginView.as_view(template_name='account/login.html'),
        name='login'),
    url(r'^logout/$', django_auth_views.LogoutView.as_view(), name='logout'),

    # password reset
    url(r'^reset/$',
        django_auth_views.PasswordResetView.as_view(
            template_name='account/password_reset.html',
            email_template_name='account/password_reset_email.html',
            subject_template_name='account/password_reset_subject.txt'
        ), name='password_reset'),
    url(r'^reset/done/$',
        django_auth_views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html'
        ), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        django_auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password_reset_confirm.html'
        ), name='password_reset_confirm'),
    url(r'^reset/complete/$',
        django_auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html'
        ),name='password_reset_complete'),

    # user profile
    url(r'^settings/$', views.UserUpdateView.as_view(), name='user_profile'),
    url(r'^settings/password/$',
        django_auth_views.PasswordChangeView.as_view(
            template_name='account/password_change.html'
        ), name='password_change'),
    url(r'^settings/password/done/$',
        django_auth_views.PasswordChangeDoneView.as_view(
            template_name='account/password_change_done.html'
        ), name='password_change_done'),
]
