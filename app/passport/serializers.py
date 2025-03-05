from rest_framework import serializers
from .models import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins 
from rest_framework import serializers
from app.passport.models import HeadPersonality, Personality, GeneralInformationImage
from django.conf import settings

class PassportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ['id', 'title', 'image', 'description']

class GeneralInformationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformationImage
        fields = ['id', 'image']

class GeneralInformationSerializer(serializers.ModelSerializer):
    images = GeneralInformationImageSerializer(many=True, read_only=True)  

    class Meta:
        model = GeneralInformation
        fields = ['id', 'title', 'description', 'images']

class InfoSerializers(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = ['id', 'title', 'description', 'images']

    def get_images(self, obj):
        """
        Возвращает полный URL всех изображений из связанных InfoObject.
        """
        request = self.context.get('request')  # Получаем request, если есть
        images = obj.infoobject_set.all()

        image_urls = []
        for image in images:
            if image.image:
                image_url = image.image.url
                # Добавляем полный URL, если request доступен
                if request:
                    image_url = request.build_absolute_uri(image_url)
                else:
                    image_url = f"{settings.MEDIA_URL}{image.image}"
                image_urls.append(image_url)

        return image_urls


class HeadPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadPersonality
        fields = ['id', 'title_personality', 'image_personality']

class PersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Personality
        fields = ['id', 'name_person', 'description_person', 'image_person','all_description_person']

class HeadPersonalityAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = HeadPersonality.objects.all()
    serializer_class = HeadPersonalitySerializer

class PersonalityAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'title', 'image', 'description']

class MapSerializers(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['title', 'image', 'link']

class VacancySerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'description_detail']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'title', 'img', 'description', 'description_detail']

class TypeInformationSerializer(serializers.ModelSerializer):
    person = PersonSerializer(many=True)

    class Meta:
        model = TypeInformation
        fields = ['id', 'title', 'img', 'description', 'person', 'link']