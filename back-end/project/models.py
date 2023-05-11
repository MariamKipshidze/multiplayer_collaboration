from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    image = models.ImageField(verbose_name=_("image"), upload_to='project/projects', blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['pk']
