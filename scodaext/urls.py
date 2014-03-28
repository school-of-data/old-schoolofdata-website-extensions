from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
import scodaext.apps.simplequiz.urls
import scodaext.apps.feedbackform.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scodaquiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^quiz/',include(scodaext.apps.simplequiz.urls)),
    url(r'^feedback/',include(scodaext.apps.feedbackform.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls'))
)


urlpatterns += staticfiles_urlpatterns()
