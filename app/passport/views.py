from rest_framework import mixins, viewsets
from .models import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .serializers import *
from rest_framework.response import Response

class PassportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {item['title']: item for item in serializer.data}
        return Response(data)

class GeneralInformationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = GeneralInformation.objects.all()
    serializer_class = GeneralInformationSerializer

class InfoAPIV(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers

class HeadPersonalityAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = HeadPersonality.objects.all()
    serializer_class = HeadPersonalitySerializer

class PersonalityAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer

class HistoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class MapViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Map.objects.all()
    serializer_class = MapSerializers

class VacancyAPIView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializers

class TypeInformationAPIView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = TypeInformation.objects.all()
    serializer_class = TypeInformationSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)