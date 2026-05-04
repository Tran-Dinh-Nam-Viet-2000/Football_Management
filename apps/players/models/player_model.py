from django.db import models
from apps.core.models.base_model import BaseModel

class FmPlayer(BaseModel):
    full_name = models.CharField(
        max_length=255,
        verbose_name="Full Name"
    )
    phone = models.CharField(
        max_length=10,
        verbose_name="Phone"
    )
    photo = models.ImageField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Photo"
    )
    national = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name="National"
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name="Birthday"
    )
    is_injury = models.BooleanField(default=False)
    height = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Height"
    )
    weight = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Weight"
    )
    is_deleted = models.BooleanField(default=False)
    position = models.ForeignKey(
        "players.FmPlayerPosition",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players",
        verbose_name="Position"
    )
    user = models.ForeignKey(
        "users.FmAuthUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="players",
        verbose_name="Auth User"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "fm_player"
        verbose_name = "fm_player"
        verbose_name_plural = "fm_players"
        ordering = ["-created_at"]