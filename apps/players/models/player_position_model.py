from django.db import models
from apps.core.models.base_model import BaseModel

class FmPlayerPosition(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Name")
    code = models.CharField(max_length=255, verbose_name="Code")

    def __int__(self):
        return f"{self.name} - {self.code}"

    class Meta:
        db_table = "fm_player_position"
        verbose_name = "fm_player_position"
        verbose_name_plural = "fm_players_positions"
        ordering = ["-created_at"]