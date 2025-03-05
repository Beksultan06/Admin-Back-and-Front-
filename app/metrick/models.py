from django.db import models

class VisitLog(models.Model):
    session_id = models.CharField(max_length=255)  # Уникальная сессия
    action = models.CharField(max_length=50)  # Например, "view", "visit"

    def __str__(self):
        return f"{self.session_id} | {self.action}"

    class Meta:
        verbose_name = 'Статистика сайта'
        verbose_name_plural = 'Статистика сайта'