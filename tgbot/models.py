from django.db import models


class User(models.Model):
    user_id = models.IntegerField("Id чата", primary_key=True, unique=True)
    username = models.CharField("Имя пользователя", max_length=32, null=True, blank=True)
    full_name = models.CharField("Полное имя", max_length=32, null=True, blank=True)
    city = models.CharField("Город", max_length=150, null=True, blank=True)
    latitude = models.CharField("Координаты широты", max_length=150, blank=True, null=True)
    longitude = models.CharField("Координаты долготы", max_length=150, blank=True, null=True)

    def __str__(self):
        return f'@{self.username}' if self.username else f'{self.user_id}'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
