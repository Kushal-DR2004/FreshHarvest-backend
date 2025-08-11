from django.urls import path
from . import views

urlpatterns = [
    path('function', views.good),                      # URL: /app/function
    path('class', views.HelloEthippia.as_view()), 
    path('c1' , views.TaskApi.as_view()),
    path('c2' , views.TaskfunApi),
]
