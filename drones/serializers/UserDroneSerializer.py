from rest_framework import serializers

from ..models.Drone import Drone


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = (
            'url',
            'name'
        )
