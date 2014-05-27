from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class UserApp(CMSApp):
    name = _("Users App")  # give your app a name, this is required
    urls = ["scodaext.apps.users.urls"]  

apphook_pool.register(UserApp)  # register your app

