from django.apps import AppConfig


class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'



from user.models import *
from user.serializers import *
cart = User.objects.all()
data = UserSimpelSerializer(cart, many=True).data
print(data)

from farmer.models import *
from farmer.serializers import *
cart = Farmer.objects.all()
data = FarmerSerializer(cart, many=True).data
print(data)

from farmer.models import *
from farmer.serializers import *
cart = Farm.objects.all()
data = FarmMinimumSerializer(cart, many=True).data
print(data)

from farmer.models import *
from farmer.serializers import *
cart = Farm.objects.all()
data = FarmSerializer(cart, many=True).data
print(data)

from farmer.models import *
from farmer.serializers import *
cart = Farmer.objects.all()
data = FarmerWithFarmSerializer(cart, many=True).data
print(data)

from product.models import *
from product.serializers import *
cart = Product.objects.all().first()
data = ProductSerializer(cart).data
print(data)

from cart.models import *
from cart.serializers import *
cart = DiscountCode.objects.all()
data = DiscountSerializer(cart, many=True).data
print(data)
from cart.models import *
from cart.serializers import *
cart = CartDetail.objects.all().first()
data = CartDetailSerializer(cart).data
print(data)

from cart.models import *
from cart.serializers import *
cart = Cart.objects.all().first()
data = CartSerializer(cart).data
print(data)

from cart.models import *
from cart.serializers import *
cart = Order.objects.all().first()
data = OrderSerializer(cart).data
print(data)






