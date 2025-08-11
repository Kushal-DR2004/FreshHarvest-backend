from rest_framework import serializers

from .models import Product , Review , LikeReview , UnlikeReview
from farmer.serializers import FarmSerializer

from user.serializers import UserSimpelSerializer

class ProductSimpleSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source = 'farm_id.farm_name')
    class Meta:
        model = Product
        fields = ('id' , 'product_name' , 'farm_name' , 'image')



class LikeSerializer(serializers.ModelSerializer):
    review_id = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all(), source='review', write_only=True
    )

    class Meta :
        model = LikeReview
        fields = ('user' , 'review_id')
        extra_kwargs = {
            'user': {'read_only': True}
        }





class UnlikeSerializer(serializers.ModelSerializer):
    review_id = serializers.PrimaryKeyRelatedField(
        queryset=Review.objects.all(), source='review', write_only=True
    )

    class Meta :
        model = UnlikeReview
        fields = ('user' , 'review_id')
        extra_kwargs = {
            'user': {'read_only': True}
        }




class ReviewSerializer(serializers.ModelSerializer):
    user = UserSimpelSerializer(read_only = True)
    likes = LikeSerializer(many = True , read_only = True)
    unlikes = UnlikeSerializer(many = True , read_only = True)

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only = True
    )

    class Meta:
        model = Review
        fields = ('id' ,'product_id' , 'rating' , 'description' , 'date' ,'user' , 'likes' , 'unlikes')



class ProductSerializer(serializers.ModelSerializer):
    farm_id = FarmSerializer(read_only = True)
    reviews = ReviewSerializer(read_only = True , many = True)
    class Meta:
        model = Product
        fields = ('product_name' , 'product_price' , 'harvested_date' , 'image' , 'farm_id' , 'reviews')






