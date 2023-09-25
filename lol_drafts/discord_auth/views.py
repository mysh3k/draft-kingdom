from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.views import View
from .secrets import auth_discord_url

# Create your views here.
class AuthDiscord(View):
    def get(self, request: HttpRequest):

        return HttpResponseRedirect(auth_discord_url)
