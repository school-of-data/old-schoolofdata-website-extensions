from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from scodaext.apps.mdplugin.models import MdPlugin
from django.utils.translation import ugettext_lazy as _

class MarkdownPlugin(CMSPluginBase):
    model = MdPlugin
    name = _("Markdown")
    render_template = "mdplugin/mdplugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(MarkdownPlugin)
