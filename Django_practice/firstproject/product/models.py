from django.db import models
from farmer.models import Farm
from user.models import User
from django.utils.timezone import now

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    farm_id = models.ForeignKey(Farm ,on_delete=models.CASCADE, related_name='farm_products')
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    harvested_date = models.DateField(default=now)
    image = models.ImageField(upload_to='product_images/' , null=False , blank=False)

class Review(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    product = models.ForeignKey(Product ,on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],max_digits=8, decimal_places=2)
    description = models.TextField()
    date = models.DateField(auto_now=True)

class LikeReview(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    review= models.ForeignKey(Review ,on_delete=models.CASCADE, related_name='likes')

class UnlikeReview(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    review= models.ForeignKey(Review ,on_delete=models.CASCADE, related_name='unlikes')