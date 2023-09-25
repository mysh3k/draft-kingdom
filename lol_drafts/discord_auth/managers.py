from django.contrib.auth import models

class DiscordUserOAuth2Manager(models.UserManager):
    def create_new_discord_user(self, discord_user, user):

        discord_user.username = user['username']
        discord_user.avatar = user['avatar']
        discord_user.global_name = user['global_name']
        discord_user.save()
        return discord_user
