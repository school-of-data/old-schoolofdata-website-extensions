from django.conf.urls import patterns, include, url
import scodaext.apps.profilemap.views

urlpatterns= patterns(
    '',
    url(r'^$', 'scodaext.apps.profilemap.views.map'),
    )
