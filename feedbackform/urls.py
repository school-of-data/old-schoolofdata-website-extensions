from django.conf.urls import patterns, include, url
import feedbackform.views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scodaquiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'feedbackform.views.fbform'),
)


