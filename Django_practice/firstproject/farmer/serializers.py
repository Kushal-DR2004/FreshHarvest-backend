from rest_framework import serializers
from .models import Farmer , Farm
from product.models import Product

class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id' , 'product_name'  , 'image' , 'product_price')

# serializers.py
class FarmMinimumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['id','farm_name' , 'about' , 'location']

class FarmerSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id' , 'farmer_name' , 'image' , 'ph_no')


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id' ,'farmer_name' ,'about' , 'ph_no' , 'about' , 'location' , 'image')



class FarmSerializer(serializers.ModelSerializer):
    farmer_id = FarmerSerializer(read_only=True) 

    class Meta:
        model = Farm
        fields = ('id' , 'farm_name' , 'about' , 'location' , 'farmer_id')


class FarmProductsSerializer(serializers.ModelSerializer):
    farm_products = ProductSimpleSerializer(many = True , read_only= True)
    #farmer_name = serializers.CharField(source='farmer_id.farmer_name', read_only=True)
    class Meta:
        model = Farm
        fields = ('id' ,'farm_name' , 'about' , 'location' , 'farm_products')


class FarmerWithFarmSerializer(serializers.ModelSerializer):
    farm = FarmProductsSerializer(many=True, read_only=True)
    class Meta:
        model = Farmer
        fields = ('id' , 'farmer_name' , 'about' , 'ph_no','location','image','farm')







