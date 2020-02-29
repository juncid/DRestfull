from rest_framework import serializers

from ..models import Drone, DroneCategory


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset=DroneCategory.objects.all(),
        slug_field='name'
    )

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Drone
        fields = (
            'url',
            'name',
            'drone_category',
            'owner',
            'manufacturing_date',
            'has_it_competed',
            'inserted_timestamp'
        )
