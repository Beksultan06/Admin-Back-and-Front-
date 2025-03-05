from rest_framework import serializers
from app.managers.models import Managers, Structure_admins, Schedule, Catalog

class ManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Managers
        fields = '__all__'

class Structure_adminsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Structure_admins
        fields = '__all__'


class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['title', 'description', 'full_name', 'date']

class CatalogSerializers(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = ['id', 'title', 'description', 'description_detail', 'date', 'image']