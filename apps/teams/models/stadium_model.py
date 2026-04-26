from django.db import models
from apps.core.models.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class FmStadium(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Stadium name"))
    address = models.CharField(max_length=255, verbose_name=_("Stadium address"))
    quality = models.IntegerField(verbose_name=_("Quality"))

    def __init__(self):
        return f"{self.name} - {self.address}"

    class Meta:
        db_table = "fm_stadium"
        verbose_name = "fm_stadium"
        verbose_name_plural = "fm_stadiums"
        ordering = ["-created_at"]