from django.conf.urls import patterns, include, url
import scodaext.apps.simplequiz.views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'scodaquiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'scodaext.apps.simplequiz.views.start'),
    url(r'^(?P<slug>[-\w]+)/$', 'scodaext.apps.simplequiz.views.quiz'),
)
