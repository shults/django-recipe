from django.db import models
from django.utils.translation import ugettext as _

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default=None, null=True, blank=True)
    slug = models.SlugField(max_length=255, default=None, blank=True)
    parent = models.ForeignKey('self', default=None, null=True,
                                blank=True, related_name='nested_category',
                                verbose_name=_('List of categories'))
    published = models.BooleanField(default=True)
    # meta info
    meta_title = models.CharField(max_length=255, default=None, null=True, blank=True)
    meta_keywords= models.CharField(max_length=255, default=None, null=True, blank=True)
    meta_description = models.TextField(default=None, null=True, blank=True)
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_title(self):
        parent_title = ''
        if (self.parent):
            parent_title = self.parent.full_title() + ' > '
        return parent_title + self.title

    # todo: override
    def __str__(self):
        return self.full_title()

    class Meta:
        verbose_name_plural = _('Categories')
