from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' , 'first_name' , 'email' , 'ph_no' , 'location' , 'image')

class UserSimpelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' , 'username' , 'image')




class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'ph_no', 'location', 'image']
        

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user





