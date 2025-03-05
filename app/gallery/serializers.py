from rest_framework import serializers
from .models import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins 
from rest_framework import serializers

class GalleryOshTourSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryOshTour
        fields = ['id', 'title', 'image', 'link']

class GalleryArchivalPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryArchivalPhotos
        fields = ['id', 'image']

class GalleryNewShapesSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryNewShapes
        fields = ['id', 'image']

class PhotoMiniSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhotoMini
        fields = ['id', 'title', 'image', "link"]
