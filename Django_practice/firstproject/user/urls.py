from django.urls import path , include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

router = DefaultRouter()
router.register(r'account', ProfileViewSet, basename='account')
#router.register(r'register' , UserRegisterAPIView ,  basename='register')



urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/' , UserRegisterAPIView.as_view()),
    path('', include(router.urls)),
]
