import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.views import View
from django.db.models import Avg
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .utils.api_calls import get_champions
from .utils.data_processor import create_match
from .models import ChampionData


# Create your views here.
class ChampionsJson(View):
    def get(self, request: HttpRequest):
        response = get_champions()
        return JsonResponse(response)


class ReceiveMatchData(View):
    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        create_match(data['metadata']['matchId'], data)
        return JsonResponse({'Done': True})


class GetAverageChampionStats(View):
    def get(self, request, champion_name):
        champion_data = ChampionData.objects.filter(championName=champion_name).aggregate(Avg('damageDealtToBuildings'), Avg('magicDamageDealtToChampions'), Avg('physicalDamageDealtToChampions'), Avg('trueDamageDealtToChampions'))
        return JsonResponse({champion_name: champion_data})