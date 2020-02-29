from rest_framework import serializers

from django.contrib.auth.models import User

from .UserDroneSerializer import UserDroneSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones = UserDroneSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'drone'
        )
