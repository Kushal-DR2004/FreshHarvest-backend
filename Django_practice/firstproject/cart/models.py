from django.db import models
from user.models import User
from product.models import Product
from django.core.validators import MaxValueValidator , MinValueValidator
from django.utils.timezone import now

# Create your models here.
class DiscountCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percent = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    active = models.BooleanField(default=True)
    

class Cart(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     discount_code = models.ForeignKey(
        DiscountCode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='carts'
    )

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(50)
        ] , default=1)
    
    def get_total_price(self):
        return self.product.product_price * self.quantity
    


    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    delivered_date = models.DateField(blank=True , null=True)
    delivered_address = models.TextField()
    discount_code = models.ForeignKey(
        DiscountCode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    discounted_price = models.DecimalField(max_digits=8, decimal_places=2 , default=0.00)

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(50)])
    price = models.DecimalField(max_digits=8, decimal_places=2)
     

