from django.db import models
from apps.core.models.base_model import BaseModel

class FmSystemRole(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Name")
    code = models.CharField(max_length=10, verbose_name="Code")

    def __init__(self):
        return self.name

    class Meta:
        #Set database name
        db_table = "fm_system_role"
        #Đặt tên bảng dạng số ít
        verbose_name = "fm_system_role"
        #Đặt tên bảng dạng số nhiều
        verbose_name_plural = "fm_system_roles"
        #Orderby
        ordering = ["created_at"]