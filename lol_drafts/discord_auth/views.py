from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.views import View
from .secrets import auth_discord_url # This should contain your discord auth link
from .utils.api_calls import auth_exchange_code, auth_get_user_data
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token


# Create your views here.
class AccountLogin(View):
    def get(self, request):
        return HttpResponseRedirect('/oauth2/login/')


class AuthDiscord(View):
    def get(self, request: HttpRequest):

        return HttpResponseRedirect(auth_discord_url)


class AuthDiscordRedirect(View):
    def get(self, request: HttpRequest):
        code = request.GET.get('code')
        credentials = auth_exchange_code(code)
        user = auth_get_user_data(credentials['access_token'])
        discord_user = authenticate(request, user=user)
        drf_token, created = Token.objects.get_or_create(user=discord_user)
        user_token = {
            'global_name': discord_user.global_name,
            'username': discord_user.username,
            'avatar': discord_user.avatar,
            'token': drf_token.key,
        }
        return JsonResponse(user_token)


class GetAuthenticatedUser(View):
    def get(self, request: HttpRequest):
        user_token = {
            'global_name': request.user.global_name,
            'username': request.user.username,
            'avatar': request.user.avatar,
            'token': request.auth.key,
        }
        return JsonResponse({'msg': 'test'})
    