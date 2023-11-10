from ..models import *

# List of attributes stored in database from API
champion_attributes_to_gather = ['championName', 'win', 'damageDealtToBuildings', 'damageDealtToObjectives', 'damageDealtToTurrets', 'damageSelfMitigated', 'goldEarned', 'goldSpent',
                                 'magicDamageDealt', 'magicDamageDealtToChampions', 'magicDamageTaken', 'physicalDamageDealt', 'physicalDamageDealtToChampions', 'physicalDamageTaken',
                                 'totalDamageDealt', 'trueDamageDealtToChampions', 'trueDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'totalDamageShieldedOnTeammates',
                                 'timeCCingOthers', 'totalTimeCCDealt', 'puuid', 'totalDamageDealtToChampions', 'totalDamageTaken', 'trueDamageDealt']


def create_match(match_id, data):
    # Get or create match
    match, created = Match.objects.get_or_create(match_str=match_id)
    # If match didn't exist and was created, create data with champions in game
    if created:
        # Fill additional match data
        match.data_version = data['info']['gameVersion']
        match.game_length = data['info']['gameDuration']
        match.save()
        for participant in data['info']['participants']:
            participant.get('win')  # I can't remember why it is here lol
            # Create Champion Data and tie it to match
            champion_data = ChampionData(match=match)
            # Loop through list defined above and set attributes to Champion Data
            for attr in champion_attributes_to_gather:
                champion_data.__setattr__(attr, participant.get(attr))
            champion_data.save()
    return match
