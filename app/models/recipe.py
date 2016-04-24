from django.db import models
from app.models.category import Category
from django.utils.translation import ugettext as _

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, verbose_name=_('Category'), default=None)
    # main data
    meta_title = models.CharField(max_length=255, default=None, null=True, blank=True)
    meta_keywords= models.CharField(max_length=255, default=None, null=True, blank=True)
    meta_description = models.TextField(default=None, null=True, blank=True)
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def category_full_title(self):
        return self.category.full_title()

    def __str__(self):
        return self.title
