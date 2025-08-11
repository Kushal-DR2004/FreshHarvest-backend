from django.db import models

# Create your models here.
class Farmer(models.Model):
    farmer_name = models.CharField(max_length=50)
    email = models.EmailField() 
    password = models.CharField(max_length=128) 
    ph_no = models.IntegerField()
    about = models.TextField()
    location = models.TextField()
    image = models.ImageField(upload_to='farmer_images/' , null=True , blank=True , default='https://www.bing.com/images/search?q=default%20profile%20picture&FORM=IQFRBA&id=5ECB59CC77F50C6345FA39079C91A16254A94879')


class Farm(models.Model):
    farm_name = models.CharField(max_length=50)
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='farm')
    about = models.TextField()
    location = models.TextField()
