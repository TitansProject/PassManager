from django.db import models


class Wifi(models.Model):
    essid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.essid + ' --> ' + self.password
