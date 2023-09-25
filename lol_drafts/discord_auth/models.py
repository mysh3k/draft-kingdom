from django.db import models

# Create your models here.
class DiscordUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=64, null=True)
    global_name = models.CharField(max_length=64, null=True)
    avatar = models.CharField(max_length=64, null=True)
    last_login = models.DateTimeField()