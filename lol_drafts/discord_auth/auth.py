from django.contrib.auth.backends import BaseBackend
from .models import DiscordUser

class DiscordAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user) -> DiscordUser:
        discord_user, created = DiscordUser.objects.get_or_create(id=user['id'])
        print(created)
        if created:
            discord_user = DiscordUser.objects.create_new_discord_user(discord_user, user)
        return discord_user

    def get_user(self, user_id):
        try:
            return DiscordUser.objects.get(pk=user_id)
        except DiscordUser.DoesNotExist:
            return None
