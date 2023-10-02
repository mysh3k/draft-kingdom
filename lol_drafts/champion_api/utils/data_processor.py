from ..models import *

champion_attributes_to_gather = ['champion', 'win', 'damageDealtToBuildings', 'damageDealtToObjectives', 'damageDealtToTurrets', 'damageSelfMitigated', 'goldEarned', 'goldSpent',
                                 'magicDamageDealt', 'magicDamageDealtToChampions', 'magicDamageTaken', 'physicalDamageDealt', 'physicalDamageDealtToChampions', 'physicalDamageTaken',
                                 'totalDamageDealt', 'trueDamageDealtToChampions', 'trueDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'totalDamageShieldedOnTeammates',
                                 'timeCCingOthers', 'totalTimeCCDealt', 'puuid']


def create_match(match_id, data):
    match, created = Match.objects.get_or_create(match_str=match_id)
    if created:
        match.data_version = data['info']['gameVersion']
        match.save()
        for participant in data['info']['participants']:
            champion_data = ChampionData.objects.create(match=match)
            for attr in champion_attributes_to_gather:
                champion_data.__setattr__(attr, participant.get(attr))
            champion_data.save()
    return match

