from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

class FmPlayerTeam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    player = models.ForeignKey(
        "players.FmPlayer",
        on_delete=models.CASCADE,
        null=True,
        related_name="fm_player_team",
        verbose_name=_("Player")
    )
    team = models.ForeignKey(
        "teams.FmTeam",
        on_delete=models.CASCADE,
        null=True,
        related_name="fm_player_team",
        verbose_name=_("Team")
    )
    left_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Left team"))
    joined_at = models.DateTimeField(verbose_name=_("Join team"))

    def __init__(self):
        return f"{self.player} - {self.team}"

    class Meta:
        db_table = "fm_player_team"
        verbose_name = "fm_player_teams"
        verbose_name_plural = "fm_player_teams"
        ordering = ["-id"]