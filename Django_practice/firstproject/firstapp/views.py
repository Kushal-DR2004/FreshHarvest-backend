from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response

# Function-based view
def good(reuest):
    return HttpResponse("i am good")

# Class-based view
class HelloEthippia(View):
    def get(self, request):
        return HttpResponse("hello ethiopia")
    

class TaskApi(APIView):
    def get(self , request):
        return Response({"message" :"the Task is done"})

@api_view(['GET'])    
def TaskfunApi(request):
    return Response({"message": "This is a GET request"})
    
