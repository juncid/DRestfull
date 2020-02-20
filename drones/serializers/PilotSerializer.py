from rest_framework import serializers

from ..models import Pilot

from .CompetitionSerializer import CompetitionSerializer


class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(
        many=True,
        read_only=True
    )
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )

    class Meta:
        model = Pilot
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'inserted_timestamp',
            'competitions'
        )
