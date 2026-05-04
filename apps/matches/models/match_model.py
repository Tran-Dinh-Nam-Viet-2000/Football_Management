from django.db import models
from apps.core.models.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class FmMatch(BaseModel):
    home_team_id = models.ForeignKey(
        "teams.FmTeam",
        on_delete=models.SET_NULL,
        null=True,
        related_name="home_matches",
        verbose_name=_("Home team")
    )
    away_team_id = models.ForeignKey(
        "teams.FmTeam",
        on_delete=models.SET_NULL,
        null=True,
        related_name="away_matches",
        verbose_name=_("Away team")
    )
    home_score = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name=_("Home score")
    )
    away_score = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name=_("Away score")
    )
    stadium = models.ForeignKey(
        "teams.FmStadium",
        on_delete=models.SET_NULL,
        null=True,
        related_name="fm_matches",
        verbose_name=_("Stadium")
    )
    match_date = models.DateTimeField(verbose_name=_("Match date"))

    def __str__(self):
        return f"**{self.match_date}** {self.home_team_id} {self.home_score} - {self.away_score} {self.away_team_id}"

    class Meta:
        db_table = "fm_match"
        verbose_name = _("fm_match")
        verbose_name_plural = _("fm_matches")
        ordering = ["-created_at"]