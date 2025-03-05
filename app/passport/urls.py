from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('generalInformation', GeneralInformationViewSet, basename='GeneralInformation')
router.register('passport', PassportViewSet, basename='passport')
router.register(r'Infos', InfoAPIV, basename='info')
router.register(r'HeadPersonalityAPI', HeadPersonalityAPI, basename='HeadPersonalityAPI')
router.register(r'PersonalityAPI', PersonalityAPI, basename='PersonalityAPI')
router.register('History', HistoryViewSet, basename='History')
router.register(r'map', MapViewSet, basename='map')
router.register(r'vacancies', VacancyAPIView, basename='vacancy')
router.register(r'type_information', TypeInformationAPIView, basename='type_information')

urlpatterns = [
    path('', include(router.urls)),
    path('PersonalityAPI/<int:pk>/', PersonalityAPI.as_view({'get': 'retrieve'}), name='PersonalityAPI'),

]

urlpatterns += router.urls
