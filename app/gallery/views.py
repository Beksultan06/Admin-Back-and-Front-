from rest_framework import mixins, viewsets
from .models import GalleryNewShapes, GalleryOshTour, GalleryArchivalPhotos
from .serializers import *

class GalleryNewShapesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryNewShapes.objects.all() 
    serializer_class = GalleryNewShapesSerializers  

class GalleryOshTourViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = GalleryOshTour.objects.all() 
    serializer_class = GalleryOshTourSerializers 

class GalleryArchivalPhotosViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GalleryArchivalPhotos.objects.all() 
    serializer_class = GalleryArchivalPhotosSerializers  

class PhotoMiniViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PhotoMini.objects.all()
    serializer_class = PhotoMiniSerializers
