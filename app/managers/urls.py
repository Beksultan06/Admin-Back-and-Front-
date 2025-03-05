from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, Structure_adminsViewSet, ScheduleViewSet, CatalogViewSet

router = DefaultRouter()
router.register(r'managers', ManagerViewSet, basename='manager',)
router.register(r'structure_admins', Structure_adminsViewSet, basename='structure_admin',)
router.register(r'schedule', ScheduleViewSet, basename='schedule')
router.register(r'catalog', CatalogViewSet, basename='catalog')


urlpatterns = [
    path('', include(router.urls)),
]