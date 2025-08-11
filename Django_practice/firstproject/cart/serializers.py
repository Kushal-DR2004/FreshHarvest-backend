from rest_framework import serializers
from .models import Cart , CartDetail , Order , OrderItem , DiscountCode

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_price' , 'image']

class CartDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True) 
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )
    class Meta:
        model = CartDetail
        fields = ['id', 'product', 'product_id', 'quantity']



class CartSerializer(serializers.ModelSerializer):
    items = CartDetailSerializer(many=True)  

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']

class ApplyDiscountCodeSerializer(serializers.ModelSerializer):
    discount_code = serializers.SlugRelatedField(
        slug_field='code',  
        queryset=DiscountCode.objects.all()
    )
    class Meta:
        model = Cart
        fields = ('id', 'discount_code', 'user')
        read_only_fields = ('id', 'user')


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer() 

    class Meta:
        model = OrderItem
        fields = ('product',
                  'quantity')


class OrderSerializer(serializers.ModelSerializer):

    items = OrderDetailSerializer(many = True , read_only = True)

    class Meta:
        model = Order
        fields = ('id' , 
                  'order_date' , 
                  'status' , 
                  'total_price' , 
                  'delivered_date' ,
                  'delivered_address' ,
                  'discounted_price' , 
                  'items')
        

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = '__all__'



class CartDiscountSerializer(serializers.ModelSerializer):
    discount_code = serializers.SlugRelatedField(
        queryset=DiscountCode.objects.filter(active=True),
        slug_field='code',
        required=True
    )

    class Meta:
        model = Cart
        fields = ['discount_code']

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = "__all__"




