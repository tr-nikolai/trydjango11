from django.db import models
from django.db.models.signals import post_save, pre_save
from django.conf import settings
from.utils import unique_slug_generator

User  = settings.AUTH_USER_MODEL

class Restaurant(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True, null=True)
    category = models.CharField(max_length=120, blank=True, null =True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null =True)


    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def rl_pre_save_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def rl_post_save_generator(sender, instance, *args, **kwargs):
#     print('saved...')
#     print(instance.timestamp)


pre_save.connect(rl_pre_save_generator, sender=Restaurant)
# post_save.connect(rl_post_save_generator, sender=Restaurant)