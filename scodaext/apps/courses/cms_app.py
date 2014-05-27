from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class CoursesApp(CMSApp):
    name= _("Courses App")
    urls = ["scodaext.apps.courses.urls"]

apphook_pool.register(CoursesApp)
