from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from restaurants.models import Restaurant


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='разделять каждый итем запятой')
    excludes = models.TextField(help_text='разделять каждый итем запятой', blank=True, null=True)
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated','-timestamp']

    def get_contents(self):
        return self.contents.split(',')

    def get_excludes(self):
        return self.excludes.split(',')

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})