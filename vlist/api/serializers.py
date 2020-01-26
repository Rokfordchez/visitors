from rest_framework import serializers
from vlist.models import UList


class UListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UList
        fields = ('id', 'visitor', 'data')


