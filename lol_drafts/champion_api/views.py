import json
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .utils.api_calls import get_champions
from .utils.data_processor import create_match
from .models import ChampionData
from .utils.champion_data import get_average_champion


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
    def get(self, request: HttpRequest, champion_name: str) -> JsonResponse:
        champion_avg = get_average_champion(champion_name)
        return JsonResponse(champion_avg)


class GetAverageTeamStats(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body)
        team_champions = data.get('team_champions', [])

        json_list = list()
        for champion_name in team_champions:
            json_list.append(get_average_champion(champion_name))
        return JsonResponse(json_list, safe=False)
