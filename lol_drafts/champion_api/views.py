import json
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
        data = json.loads(request.body)                             # Get data from POST request
        team_champions = data.get('team_champions', [])             # Get list of champions from request

        json_list = list()
        for champion_name in team_champions:
            json_list.append(get_average_champion(champion_name))
        return JsonResponse(json_list, safe=False)


class GetAverageGameStats(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body)                             # Get data from POST request
        # Get list of champions in blue team, could do Loop with Conditionals to avoid 2 List Comprehensions but I don't think performace will be issue
        blue_team = [pick for key, pick in data.items() if key.startswith('Blue_pick') and pick is not None]
        blue_list = list()
        for champion_name in blue_team:
            blue_list.append(get_average_champion(champion_name))

        # Get list of champions in red team
        red_team = [pick for key, pick in data.items() if key.startswith('Red_pick') and pick is not None]
        red_list = list()
        for champion_name in red_team:
            red_list.append(get_average_champion(champion_name))
        # Merge data into dictionary
        game_dict = {
            'blue_team': blue_list,
            'red_team': red_list
        }
        return JsonResponse(game_dict, safe=False)
