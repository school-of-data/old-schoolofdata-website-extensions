from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scodaquiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^quiz/',include(scodaext.apps.simplequiz.urls)),
    # url(r'^feedback/',include(scodaext.apps.feedbackform.urls)),
)


urlpatterns += staticfiles_urlpatterns()
