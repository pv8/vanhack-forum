from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    url('^forum/', include('forum.urls')),
    url('^account/', include('account.urls')),

    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^admin/', admin.site.urls),

    url(r'^$', RedirectView.as_view(pattern_name='posts_list', permanent=False), name='home'),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns