from django.db import models
from apps.core.models.base_model import BaseModel

class FmAuthUser(BaseModel):
    user_name = models.CharField(max_length=255, verbose_name="Username")
    email = models.EmailField(max_length=255, verbose_name="Email")
    password = models.TextField(verbose_name="Password")
    is_deleted = models.BooleanField(default=False)
    role = models.ForeignKey(
        "users.FmSystemRole",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="fm_auth_users",
        verbose_name="Role"
    )

    def __init__(self):
        return self.user_name

    class Meta:
        db_table = "fm_auth_user"
        verbose_name = "fm_auth_user"
        verbose_name_plural = "fm_auth_users"
        ordering = ["-created_at"]