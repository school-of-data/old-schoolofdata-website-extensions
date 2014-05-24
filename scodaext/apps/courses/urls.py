from django.conf.urls import patterns, include, url
import scodaext.apps.courses.views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'scodaquiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'scodaext.apps.courses.views.start'),
    url(r'^(?P<course>[-\w]+)/$', 'scodaext.apps.courses.views.course'),
    url(r'^(?P<course>[-\w]+)/(?P<module>[-\w]+)/$',
        'scodaext.apps.courses.views.module'),
    url(r'^module/(?P<module>[-\w]+)/edit/$',
        'scodaext.apps.courses.views.editmodule'),
    url(r'^(?P<course>[-\w]+)/edit/$',
        'scodaext.apps.courses.views.editcourse'),
    url(r'^create/$',
        'scodaext.apps.courses.views.createcourse'),
    url(r'^module/create/$',
        'scodaext.apps.courses.views.createmodule'),

)
