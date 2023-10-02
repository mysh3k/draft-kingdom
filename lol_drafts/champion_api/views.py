import json

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .utils.api_calls import get_champions
from .utils.data_processor import create_match


# Create your views here.
class ChampionsData(View):
    def get(self, request: HttpRequest):
        response = get_champions()
        return JsonResponse(response)


class ReceiveMatchData(View):
    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        create_match(data['metadata']['matchId'], data)
        return JsonResponse({'Done': True})
