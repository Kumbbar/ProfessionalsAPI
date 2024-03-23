from .models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    PersonCode = serializers.IntegerField(source='id')
    PersonRole = serializers.CharField(source='role')
    LastSecurityPointNumber = serializers.IntegerField(source='skud_number')
    LastSecurityPointDirection = serializers.CharField(source='skud_direction')
    LastSecurityPointTime = serializers.DateTimeField(source='skud_datetime')

    class Meta:
        model = Person
        fields = (
            'PersonCode',
            'PersonRole',
            'LastSecurityPointNumber',
            'LastSecurityPointDirection',
            'LastSecurityPointTime'
        )


class PersonAdminSerializerAdmin(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'role',
            'skud_number',
            'skud_direction',
            'skud_datetime',
        )