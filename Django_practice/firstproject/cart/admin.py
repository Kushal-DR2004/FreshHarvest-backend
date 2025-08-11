from django.contrib import admin

from .models import Cart
from .models import CartDetail
from .models import DiscountCode
from .models import Order
from .models import OrderItem

admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(DiscountCode)
admin.site.register(Order)
admin.site.register(OrderItem)


