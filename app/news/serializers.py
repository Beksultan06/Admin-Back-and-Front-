from rest_framework import serializers
from app.news.models import News, Media, NewsNok, TourismNok, AboutNok, Project, NewsObject

class NewsSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'description','date','image','first_paragraph','second_paragraph','general_paragraph','img']

    def get_img(self, obj):
        """
        Возвращает полный URL всех изображений из связанных NewsObject.
        """
        request = self.context.get('request')
        img = obj.newsobject_set.all()

        image_urls = []
        for image in img:
            if image.image:
                image_url = image.image.url
                if request:
                    image_url = request.build_absolute_uri(image_url)
                else:
                    image_url = f"{settings.MEDIA_URL}{image.image.url}"
                image_urls.append(image_url)

        return image_urls


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id','title_media','description_media','date_media','image_media','link',]

class NewsNokSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsNok
        fields = ['id','title','description','date','photo',]

class TourismNokSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismNok
        fields = ['id','title','description','image',]

class AboutNokSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutNok
        fields = ['id','description','image',]


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'image', 'date', 'description', 'description_detail']