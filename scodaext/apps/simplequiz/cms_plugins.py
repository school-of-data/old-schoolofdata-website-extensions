from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from scodaext.apps.simplequiz.models import QuizPlugin
from django.utils.translation import ugettext as _

class CMSPollPlugin(CMSPluginBase):
    model = QuizPlugin  # Model where data about this plugin is saved
    name = _("Quiz Plugin")  # Name of the plugin
    render_template = "simplequiz/plugin.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSPollPlugin)  # register
