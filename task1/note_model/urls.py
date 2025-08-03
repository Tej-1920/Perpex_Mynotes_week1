from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('notes',NoteViewSet,basename='note')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/token/',obtain_auth_token,name='api_token_auth'),
]