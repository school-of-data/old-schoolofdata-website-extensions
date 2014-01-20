from django.conf.urls import patterns, include, url
import simplequiz.views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'scodaquiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'simplequiz.views.start'),
    url(r'^quiz/(?P<slug>[-\w]+)/$', 'simplequiz.views.quiz'),
)
