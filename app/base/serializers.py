from rest_framework import serializers
from app.base.models import We_Invite_To_View, Gallery, Banner, LatestNews, Settings

class We_Invite_To_ViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = We_Invite_To_View
        fields = [
            'title', 'title_place', 'description_place',
            'date_place', 'image_place'
        ]
        
class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = [
            'title_gallery', 'photo'
        ]

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['title', 'image', 'full_name', 'description']
        
class LatestNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = LatestNews
        fields = 'title', 'image', 'description', 'date'


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = [
            'id', 'logo', 'title_logo', 'location', 'phone', 'link_phone', 'link_insta',
            'link_telegram', 'link_watapp', 'link_youtube', 'link_facebook', 'end_news',
            'preview', 'gallery', 'news_nookat', 'title_cmi', 'project_title', 'title_admin',
            'location_name', 'anti_corup'
        ]