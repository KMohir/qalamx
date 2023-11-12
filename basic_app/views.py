from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from basic_app.models import *
from basic_app.serializers import *


class ViloyatList(generics.ListCreateAPIView):
    queryset = Viloyat.objects.all()
    serializer_class = ViloyatSerializer


class TumanList(generics.ListCreateAPIView):
    queryset = Tuman.objects.all()
    serializer_class = TumanSerializer
    # filter_backends = (filters.DjangoFilterBackend)
    # filterset_fields = ('tuman')


class StansiyaList(generics.ListCreateAPIView):
    queryset = Stansiya.objects.all()
    serializer_class = StansiyaSerializer


class OsimlikList(generics.ListCreateAPIView):
    queryset = Osimlik.objects.all()
    serializer_class = OsimlikSerialzier


class HashorotList(generics.ListCreateAPIView):
    queryset = Hashorot.objects.all()
    serializer_class = HashorotSerializer


class DataHashorotList(generics.ListCreateAPIView):
    queryset = DataHashorot.objects.all()
    serializer_class = DataHashorotSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('viloyat', 'tuman', 'stansiya', 'osimlik_nomi', 'hashorot', 'vaqt', 'statistica', 'vlajnost')


class dataSList(generics.ListCreateAPIView):
    queryset = data.objects.all()
    serializer_class = dataSerializer
