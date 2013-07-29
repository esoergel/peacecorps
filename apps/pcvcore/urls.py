from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import UpdatePCVProfile

# urls prefixed by /user/
urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name="base.html")),
    url(r'^teacherhome/$', TemplateView.as_view(template_name="home/teacherhome.html")),
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name':"user/login.html"}, name="login"
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name="logout"
    ),
    url(r'^update/$', UpdatePCVProfile.as_view(), name="update_profile"),
)
