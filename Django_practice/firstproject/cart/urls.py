from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cartitems', GetcartView , basename='carts')
router.register(r'cartdetails' , CartDetailsView , basename='cart-details')
router.register(r'orders' , PlaceOrderViewSet , basename='order')
router.register(r'discountapply' , ApplyDiscountCodeViewSet , basename="discount-apply")
router.register(r'discounts' , DiscountViewSet , basename="discount")


urlpatterns = [
    path('' , include(router.urls)),
    #path('<int:pk>/' ,CartDetailsView.as_view()),
    #path('<int:pk>/increase/' ,CartItemIncreseView.as_view()),
    #path('<int:pk>/decrease/' ,CartItemDecreaseView.as_view()),
    #path('' ,GetCartView.as_view()),
    #path('orders/' , PlaceOrderView.as_view()),
    #path('discount/apply' , ApplyDiscountCodeView.as_view())   
]