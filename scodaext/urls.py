from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
import simplequiz.urls
import feedbackform.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scodaquiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include(simplequiz.urls)),
    url(r'^feedback/',include(feedbackform.urls)),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += staticfiles_urlpatterns()
