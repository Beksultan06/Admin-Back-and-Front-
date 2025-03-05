from rest_framework import viewsets, mixins
from .models import Managers, Structure_admins, Schedule, Catalog
from .serializers import ManagerSerializers, Structure_adminsSerializers, ScheduleSerializers, CatalogSerializers
    
class ManagerViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin):
    queryset = Managers.objects.all()
    serializer_class = ManagerSerializers

class Structure_adminsViewSet(viewsets.GenericViewSet,
                              mixins.ListModelMixin):
    queryset = Structure_admins.objects.all()
    serializer_class = Structure_adminsSerializers


class  ScheduleViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers

class CatalogViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializers
