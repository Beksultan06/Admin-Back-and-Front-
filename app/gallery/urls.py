from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryOshTourViewSet, GalleryArchivalPhotosViewSet, GalleryNewShapesViewSet, PhotoMiniViewSet

router = DefaultRouter()
router.register(r'GalleryNewShapes', GalleryNewShapesViewSet, basename='GalleryNewShapes')
router.register(r'GalleryOshTour', GalleryOshTourViewSet, basename='GalleryOshTour',)
router.register(r'GalleryArchivalPhotos', GalleryArchivalPhotosViewSet, basename='GalleryArchivalPhotos',)
router.register(r'PhotoMiniKg', PhotoMiniViewSet, basename='PhotoKg')

urlpatterns = [
    path('', include(router.urls)),
]