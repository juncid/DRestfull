from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.Serializer):
    class Meta:
        model = Toy
        fields = ('id',
                  'name',
                  'description',
                  'release_date',
                  'toy_category',
                  'was_included_in_home')
