from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class FeedbackApp(CMSApp):
    name = _("Feedback Form")  # give your app a name, this is required
    urls = ["scodaext.apps.feedbackform.urls"]  # link your app to url configuration(s)

apphook_pool.register(FeedbackApp)  # register your app
