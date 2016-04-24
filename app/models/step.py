from django.db import models
from app.models import Recipe
from django.utils.translation import ugettext as _

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1 << 16, blank=True,
                                    null=True, default=None)
    recipe = models.ForeignKey(Recipe)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
