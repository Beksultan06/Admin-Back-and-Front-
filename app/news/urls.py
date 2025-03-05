from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.news.views import NewsAPI, MediaAPI, TourismNokAPI, ProjectViewSet

router = DefaultRouter()
router.register(r'news', NewsAPI, basename='news')
router.register(r'media', MediaAPI, basename='media')
router.register(r'tourism-nok', TourismNokAPI, basename='tourism_nok')
router.register(r'projects', ProjectViewSet, basename='project')


urlpatterns = [
    path('', include(router.urls)),
]