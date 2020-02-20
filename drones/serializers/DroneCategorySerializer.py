from rest_framework import serializers

from ..models import DroneCategory


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
