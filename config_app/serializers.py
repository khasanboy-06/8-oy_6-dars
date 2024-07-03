from rest_framework import serializers
from .models import Hudud, Qurilish_binosi, Qurilish_tashkiloti

class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = '__all__'


class QurilishbinosiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qurilish_binosi
        fields = '__all__'


class Qurilish_tashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qurilish_tashkiloti
        fields = '__all__'