from rest_framework import serializers

from .models import DroneCategory, Drone, Pilot, Competition
import drones.views


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='drone_detail'
    )

    class Meta:
        model = DroneCategory
        fields = [
            'url',
            'pk',
            'name',
            'drones'
        ]

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField()