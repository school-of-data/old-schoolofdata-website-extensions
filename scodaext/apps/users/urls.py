from django.conf.urls import patterns, include, url
import scodaext.apps.users.views
import django.contrib.auth.views

urlpatterns = patterns(
    '',
    url(r'^$',
        'scodaext.apps.users.views.start'),
    url(r'^new/$',
        'scodaext.apps.users.views.new'),
    url(r'^login/$',
        'scodaext.apps.users.views.login'),
    url(r'^logout/$',
        'scodaext.apps.users.views.logout'),
    url(r'^edit/$',
        'scodaext.apps.users.views.editprofile'),
    url(r'^password$',
        'scodaext.apps.users.views.password'),
    url(r'^(?P<username>[-\w]+)/$',
        'scodaext.apps.users.views.profile'),
    url(r'^(?P<username>[-\w]+)/badges/$',
        'scodaext.apps.users.views.badges'),
    )
