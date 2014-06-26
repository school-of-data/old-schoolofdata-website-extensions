from django.db import models

from cms.models.pluginmodel import CMSPlugin

class MdPlugin(CMSPlugin):
    markdown = models.TextField()


