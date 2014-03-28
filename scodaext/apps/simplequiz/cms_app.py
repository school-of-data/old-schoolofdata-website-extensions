from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class QuizApp(CMSApp):
    name = _("Quiz App")  # give your app a name, this is required
    urls = ["scodaext.apps.simplequiz.urls"]  # link your app to url configuration(s)

apphook_pool.register(QuizApp)  # register your app
