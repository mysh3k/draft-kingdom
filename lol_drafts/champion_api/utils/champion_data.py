from ..models import ChampionData
from django.db.models import Avg


def get_average_champion(champion_name: str) -> dict:
    # Filter data based on 'champion_name' passed as parameter
    champion_data = ChampionData.objects.filter(championName__iexact=champion_name)
    # Calculate average stats from queryset
    champion_avg = champion_data.aggregate(Avg('physicalDamageDealtToChampions'), Avg('magicDamageDealtToChampions'),
                                           Avg('trueDamageDealtToChampions'),
                                           Avg('physicalDamageTaken'), Avg('magicDamageTaken'), Avg('trueDamageTaken'),
                                           Avg('damageDealtToTurrets'), Avg('damageDealtToObjectives'),
                                           Avg('damageDealtToBuildings'),
                                           Avg('timeCCingOthers'), Avg('totalTimeCCDealt'),
                                           Avg('totalHeal'), Avg('totalHealsOnTeammates'),
                                           Avg('totalDamageShieldedOnTeammates'), Avg('damageSelfMitigated'))
    number_of_games = champion_data.count()                     # Data sample
    number_of_wins = champion_data.filter(win=True).count()     # Number of wins in sample
    # Wrapping data to dictionary
    data_to_return = {
        'champion': champion_name,
        'sample_size': number_of_games,
        'wins': number_of_wins,
        'stats': champion_avg
    }
    return data_to_return
