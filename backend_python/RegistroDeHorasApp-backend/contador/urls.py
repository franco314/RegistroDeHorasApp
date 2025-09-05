from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistroDeHorasViewSet
from .views_auth import UserRegisterView  

router = DefaultRouter()
router.register(r'registros', RegistroDeHorasViewSet, basename='registro')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterView.as_view(), name='user-register'),  
]
