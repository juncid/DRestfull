from django.db import models

from .Drone import Drone
from .Pilot import Pilot


class Competition(models.Model):
    pilot = models.ForeignKey(
        Pilot,
        related_name='competitions',
        on_delete=models.CASCADE
    )
    drone = models.ForeignKey(
        Drone,
        on_delete=models.CASCADE
    )
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()

    class Meta:
        ordering = ('-distance_in_feet', )