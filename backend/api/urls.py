from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register('PersonLocations', views.PersonGetViewSet, basename='PersonLocations')
router.register('PersonLocationsAdmin', views.PersonViewSet, basename='PersonLocationsAdmin')


urlpatterns = [
    path('', include(router.urls)),
    path('rest/', include('rest_framework.urls')),
    path('PersonLocationsUpdate/', views.UpdatePersonsPositions.as_view()),

    ]
