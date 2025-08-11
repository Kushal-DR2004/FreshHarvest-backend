from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'productitems', ProductViewSet, basename='product')
router.register(r'reviews' , ProductReviewSet)

urlpatterns = [
     path('' , include(router.urls)),
    #path('', ProductList.as_view()),
    #path('<int:pk>/' ,ProductDetail.as_view()),
    #path('search/', ProductSearchAPIView.as_view()),
    #path('review/', ReviewCreateView.as_view()),
    #path('review/<int:pk>/' , ReviewDeleteView.as_view()),
    #path('review/<int:pk>/like/', ReviewLikeView.as_view()),
    #path('review/<int:pk>/unlike/', ReviewUnlikeView.as_view())
    
]