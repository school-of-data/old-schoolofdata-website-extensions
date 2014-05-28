from django.conf.urls import patterns, include, url
import scodaext.apps.users.views

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
    url(r'^(?P<username>)/$',
        'scodaext.apps.users.views.profile'),
    url(r'^(?P<username>)/edit/$',
        'scodaext.apps.users.views.editprofile')
    )
