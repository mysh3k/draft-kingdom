from django.db import models
from .managers import DiscordUserOAuth2Manager

# Create your models here.
class DiscordUser(models.Model):
    objects = DiscordUserOAuth2Manager()

    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=64, null=True)
    global_name = models.CharField(max_length=64, null=True)
    avatar = models.CharField(max_length=64, null=True)
    last_login = models.DateTimeField(null=True)

    def is_authenticated(self, request):
        return True