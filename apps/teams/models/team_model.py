from django.db import models
from apps.core.models.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class FmTeam(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Team name"))
    headquarter = models.CharField(max_length=255, verbose_name=_("Team headquarter"))
    stadium = models.OneToOneField(
        "teams.FmStadium",
        on_delete=models.CASCADE,
        related_name="teams",
        verbose_name=_("Stadium")
    )
    coach = models.OneToOneField(
        "teams.FmCoach",
        on_delete=models.CASCADE,
        related_name="teams",
        verbose_name=_("Coach")
    )

    def __init__(self):
        return f"{self.name} - {self.headquarter}"

    class Meta:
        db_table = "fm_team"
        verbose_name = "fm_team"
        verbose_name_plural = "fm_teams"
        ordering = ["-created_at"]