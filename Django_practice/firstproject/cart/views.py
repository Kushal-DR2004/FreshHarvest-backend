from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartDetailSerializer , CartSerializer , OrderSerializer , DiscountSerializer ,ApplyDiscountCodeSerializer
from .models import Cart , CartDetail , DiscountCode , Order ,OrderItem

from rest_framework.permissions import IsAuthenticated
from decimal import Decimal
from rest_framework import status, viewsets
from rest_framework.decorators import action


class CartDetailsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartDetailSerializer

    def perform_create(self, serializer):
        cart , _= Cart.objects.get_or_create(user=self.request.user)
        product = serializer.validated_data.get('product')
        existing_detail = CartDetail.objects.filter(cart=cart, product=product).first()

        if existing_detail:
            existing_detail.quantity += 1
            existing_detail.save()
        else:
            serializer.save(cart = cart)

    @action(detail=True, methods=['put'], url_path='increase')
    def increase(self, request, pk = None): 
        cartDetails = CartDetail.objects.get(id = pk)

        cartDetails.quantity += 1
        cartDetails.save()
        return Response({"message": "Quantity increased successfully."})
    

    @action(detail=True, methods=['put'], url_path='decrease')
    def decrease(self, request, pk = None): 
        cartDetails = CartDetail.objects.get(id = pk)

        cartDetails.quantity -= 1

        if cartDetails.quantity == 0:
            cartDetails.delete()
            return Response({"message": "Quantity decreased successfully."})
        cartDetails.save()
        return Response({"message": "Quantity decreased successfully."})

    
        
class GetcartView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    

class PlaceOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user = self.request.user).prefetch_related('items')
    
    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=self.request.user)
        cart_items = CartDetail.objects.filter(cart=cart)

        total_price = Decimal(0.00)
        for item in cart_items:
                total_price += item.get_total_price()

        discount = None
        discounted_price = Decimal()


        discount_id = cart.discount_code

        if discount_id:
            try:
                discount = DiscountCode.objects.get(id=discount_id.id)
                if discount.discount_percent:
                    discount_amount = (Decimal(discount.discount_percent) / Decimal(100)) * total_price
                    discounted_price = total_price - discount_amount
            except DiscountCode.DoesNotExist:
                return Response({"error": "Invalid discount code or it already expired."})
            
        serializer = OrderSerializer(data = request.data)
        
        if serializer.is_valid():
            print(cart_items)
            order = serializer.save(user = self.request.user , total_price = total_price , discounted_price = discounted_price)
            for item in cart_items:
                
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.product_price
                )

            cart_items.delete()
            #code = cart.discount_code
            cart.discount_code = None
            cart.save()
            
            return Response({"message": "Order placed successfully." })
        
        return Response(serializer.errors, status=400)
    

class ApplyDiscountCodeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplyDiscountCodeSerializer

    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)
    
class ApplyDiscountCodeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplyDiscountCodeSerializer

    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)
    

class DiscountViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DiscountSerializer
    queryset = DiscountCode.objects.all()





"""class CartDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self , request , pk):

        user = request.user
       
        cart , _= Cart.objects.get_or_create(user=user)
        
        data = request.data.copy()
        data['product_id'] = pk
    
        serializer = CartDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save(cart=cart) 
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CartItemIncreseView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self , request , pk):
        cartDetails = CartDetail.objects.get(id = pk)

        cartDetails.quantity += 1
        cartDetails.save()
        return Response({"message": "Quantity increased successfully."})
    

class CartItemDecreaseView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self , request , pk):
        cartDetails = CartDetail.objects.get(id = pk)

        cartDetails.quantity -= 1
        if cartDetails.quantity == 0:
            cartDetails.delete()
            return Response({"message": "cart item deleted successfully."})
        cartDetails.save()
        return Response({"message": "Quantity decrease successfully."})"""
        
"""class GetCartView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        user = request.user
        cart , _= Cart.objects.get_or_create(user=user)

        serializer = CartSerializer(cart)
        return Response(serializer.data)"""
    
"""
class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user).prefetch_related('items')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
            cart_items = CartDetail.objects.filter(cart=cart)
            
            delivered_address = request.data.get("delivered_address")
            discount_id = request.data.get("discount_code")

        
            #total_price = 0.0
            total_price = Decimal(0.00)
            for item in cart_items:
                total_price += item.get_total_price()

            discount = None
            #discounted_price = 0.0
            discounted_price = Decimal(0.00)

            if discount_id:
                try:
                    discount = DiscountCode.objects.get(id=discount_id)
                    if discount.percentage:
                        discount_amount = (Decimal(discount.percentage) / Decimal(100)) * total_price
                        discounted_price = total_price - discount_amount
                except DiscountCode.DoesNotExist:
                    return Response({"error": "Invalid discount code or it already expired."})

            
            order = Order.objects.create(
                user=user,
                delivered_address=delivered_address,
                total_price=total_price,
                discount_code=discount,
                discounted_price=discounted_price,
                
            )
            cart.discount_code = None
            cart.save()

        
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.product_price
                )
            cart_items.delete()
            

            return Response({"message": "Order placed successfully." })
        except:
            return Response({"error" : "error in creating order"})
        
"""

"""class ApplyDiscountCodeView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found."})

        serializer = CartDiscountSerializer(cart, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Discount code applied successfully."})
        return Response(serializer.errors)
"""
    

        