from rest_framework import serializers

from basic_app.models import Viloyat, Tuman
from basic_app import models


class ViloyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viloyat
        fields = '__all__'


class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = '__all__'


class StansiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stansiya
        fields = '__all__'


class OsimlikSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.Osimlik
        fields = '__all__'


class HashorotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hashorot
        fields = '__all__'


class DataHashorotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataHashorot
        fields = '__all__'


class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.data
        fields = '__all__'
