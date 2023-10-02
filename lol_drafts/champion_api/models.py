from django.db import models


# Create your models here.
class Match(models.Model):
    match_str = models.CharField(max_length=64)
    data_version = models.CharField(max_length=16)


class ChampionData(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    puuid = models.CharField(max_length=256)
    championName = models.CharField(max_length=32)
    win = models.BooleanField()

    damageDealtToBuildings = models.IntegerField()
    damageDealtToObjectives = models.IntegerField()
    damageDealtToTurrets = models.IntegerField()
    damageSelfMitigated = models.IntegerField()

    goldEarned = models.IntegerField()
    goldSpent = models.IntegerField()

    magicDamageDealt = models.IntegerField()
    magicDamageDealtToChampions = models.IntegerField()
    magicDamageTaken = models.IntegerField()

    physicalDamageDealt = models.IntegerField()
    physicalDamageDealtToChampions = models.IntegerField()
    physicalDamageTaken = models.IntegerField()

    totalDamageDealt = models.IntegerField()
    totalDamageDealtToChampions = models.IntegerField()
    totalDamageTaken = models.IntegerField()

    trueDamageDealt = models.IntegerField()
    trueDamageDealtToChampions = models.IntegerField()
    trueDamageTaken = models.IntegerField()

    totalHeal = models.IntegerField()
    totalHealsOnTeammates = models.IntegerField()
    totalDamageShieldedOnTeammates = models.IntegerField()
    timeCCingOthers = models.IntegerField()
    totalTimeCCDealt = models.IntegerField()
