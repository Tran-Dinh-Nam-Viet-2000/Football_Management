from django.db import models
from apps.core.models.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class FmCoach(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_("Full name"))
    phone = models.CharField(max_length=10, unique=True, verbose_name=_("Phone"))
    photo = models.ImageField(null=True, blank=True, verbose_name=_("Photo"))
    level = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("Level"))
    experience_years = models.IntegerField(null=True, blank=True, verbose_name=_("Experience Years"))
    user = models.OneToOneField(
        "users.FmAuthUser",
        on_delete=models.CASCADE,
        related_name="fm_coaches",
        verbose_name=_("User")
    )

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = "fm_coach"
        verbose_name = "fm_coach"
        verbose_name_plural = "fm_coaches"
        ordering = ["-created_at"]