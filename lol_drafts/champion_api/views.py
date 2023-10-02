from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .utils.api_calls import get_champions


# Create your views here.
class ChampionsData(View):
    def get(self, request: HttpRequest):
        response = get_champions()
        return JsonResponse(response)

