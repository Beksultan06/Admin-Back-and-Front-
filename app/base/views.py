from django.shortcuts import render
from app.base.serializers import We_Invite_To_ViewSerializers, GallerySerializers, BannerSerializers, LatestNewsSerializers, SettingsSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from app.base.models import We_Invite_To_View, Gallery, Banner, LatestNews, Settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

class We_Invite_To_ViewViewSet(GenericViewSet, 
                               mixins.ListModelMixin):
    queryset = We_Invite_To_View.objects.all()
    serializer_class = We_Invite_To_ViewSerializers

class GalleryViewSet(GenericViewSet, 
                               mixins.ListModelMixin):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers

class BannerAPI(GenericViewSet,
                       mixins.ListModelMixin):
    queryset = Banner.objects.all() 
    serializer_class = BannerSerializers

class LatestNewsAPI(GenericViewSet,
                    mixins.ListModelMixin):
    queryset = LatestNews.objects.all()
    serializer_class = LatestNewsSerializers

class SettingsAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer