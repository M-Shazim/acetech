from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True)
    whatsapp_number = models.CharField(max_length=15)

    def __str__(self):
        return self.title
