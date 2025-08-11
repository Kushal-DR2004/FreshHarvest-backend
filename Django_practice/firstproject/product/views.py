from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.decorators import action


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'description']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSimpleSerializer
        return ProductSerializer


class ProductReviewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'], url_path='like')
    def like(self, request, pk): 
        data = request.data.copy()
        data['review_id'] = pk

        existing_like = LikeReview.objects.filter(user = self.request.user , review = Review.objects.get(id = pk))
        existing_unlike = UnlikeReview.objects.filter(user =self.request.user, review = Review.objects.get(id = pk))

        if existing_unlike:
            existing_unlike.delete()

        if existing_like:
            existing_like.delete()
            return Response({'message': 'like removed successfully.'})
        else:
            serializer = LikeSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)
            return Response(serializer.errors)
        
        
    @action(detail=True, methods=['post'], url_path='unlike')
    def like(self, request, pk): 
        data = request.data.copy()
        data['review_id'] = pk

        existing_like = LikeReview.objects.filter(user = self.request.user , review = Review.objects.get(id = pk))
        existing_unlike = UnlikeReview.objects.filter(user =self.request.user, review = Review.objects.get(id = pk))

        if existing_like:
            existing_like.delete()

        if existing_unlike:
            existing_unlike.delete()
            return Response({'message': 'Runlike removed sucessfully successfully.'})
        else:
            serializer = UnlikeSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data)

            return Response(serializer.errors)
    


"""
class ProductList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSimpleSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serialize = ProductSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.error)
            

class ProductDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request , pk):
        products = Product.objects.get(pk = pk)

        if products:
            serializer = ProductSerializer(products)
            return Response(serializer.data)
        return Response(serializer.error)
    

    
class ProductSearchAPIView(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSimpleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name','description']
    """
    

"""class ReviewCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    

class ReviewDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self , request , pk):
        try:
            review = Review.objects.get(pk = pk)
        except Review.DoesNotExist:
            return Response({"message" , "review does not exists"})
        
        if review.user != request.user:
            return Response({"message" , "you are not allowed"})
        
        review.delete()
        return Response({"message" : "review deleted sucessfully"})
    
    def patch(self , request , pk):
        review = Review.objects.get(pk = pk)
        try:
            review = Review.objects.get(pk = pk)
        except Review.DoesNotExist:
            return Response({"message" , "review does not exists"}) 
        
        if review.user != request.user:
            return Response({"message" , "you are not allowed to edit"})
        
        serializer = ReviewSerializer(review , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

"""

    
"""class ReviewLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self , request , pk):
        data = request.data.copy()
        data['review_id'] = pk
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    


class ReviewUnlikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self , request , pk):
        data = request.data.copy()
        data['review_id'] = pk
        serializer = UnlikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)"""