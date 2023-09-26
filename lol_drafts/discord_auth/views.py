from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.views import View
from .secrets import auth_discord_url # This should contain your discord auth link
from .utils.api_calls import auth_exchange_code, auth_get_user_data
from  django.contrib.auth import authenticate, login


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
        login(request, discord_user)
        return JsonResponse(user)


class GetAuthenticatedUser(View):
    def get(self, request: HttpRequest):
        return JsonResponse({'msg': 'test'})
    