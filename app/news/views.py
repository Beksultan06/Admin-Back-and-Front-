from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from app.news.models import News, Media, NewsNok, TourismNok, AboutNok, Project
from app.news.serializers import NewsSerializer, MediaSerializer, NewsNokSerializer, AboutNokSerializer, TourismNokSerializer, ProjectSerializers
# Create your views here.

class NewsAPI(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin
                ):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class MediaAPI(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin
                ):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class TourismNokAPI(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin
                ):

    queryset = TourismNok.objects.all()
    serializer_class = TourismNokSerializer

class ProjectViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers