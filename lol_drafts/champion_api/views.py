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
        champion_data = ChampionData.objects.filter(championName__iexact=champion_name)
        champion_avg = champion_data.aggregate(Avg('physicalDamageDealtToChampions'), Avg('magicDamageDealtToChampions'), Avg('trueDamageDealtToChampions'),
                                               Avg('physicalDamageTaken'), Avg('magicDamageTaken'), Avg('trueDamageTaken'),
                                               Avg('damageDealtToTurrets'), Avg('damageDealtToObjectives'), Avg('damageDealtToBuildings'),
                                               Avg('timeCCingOthers'), Avg('totalTimeCCDealt'),
                                               Avg('totalHeal'), Avg('totalHealsOnTeammates'), Avg('totalDamageShieldedOnTeammates'), Avg('damageSelfMitigated'))
        number_of_games = champion_data.count()
        number_of_wins = champion_data.filter(win=True).count()
        return JsonResponse({'sample_size': number_of_games, 'wins': number_of_wins, champion_name: champion_avg})
