from django.urls import path
from rest_framework.routers import DefaultRouter
from app.base.views import We_Invite_To_ViewViewSet, GalleryViewSet, BannerAPI, LatestNewsAPI, SettingsAPI

router = DefaultRouter()
router.register(r'we-invite-to-view', We_Invite_To_ViewViewSet, basename="we-invite-to-view")
router.register(r'gallery', GalleryViewSet, basename="gallery")
router.register(r'banner', BannerAPI, basename='banner')
router.register(r'latest-news', LatestNewsAPI, basename='latest-news')
router.register(r'settings', SettingsAPI, basename='settings')


urlpatterns = [
    
]

urlpatterns += router.urls