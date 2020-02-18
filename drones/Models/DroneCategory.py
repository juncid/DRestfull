from django.db import models


class DroneCategory(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
