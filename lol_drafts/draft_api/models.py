from django.db import models
from discord_auth.models import DiscordUser

# Create your models here.
class Draft(models.Model):
    created_by = models.ForeignKey(DiscordUser, on_delete=models.DO_NOTHING)
    is_public = models.BooleanField(default=False)
    draft_data = models.JSONField()

