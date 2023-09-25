from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser

class DiscordAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user) -> DiscordUser:
        discord_user, created = DiscordUser.objects.get_or_create(id=user['id'])
        if created:
            user.username = user['username']
            user.avatar = user['avatar']
            user.global_name = user['global_name']
            user.save()
        return discord_user