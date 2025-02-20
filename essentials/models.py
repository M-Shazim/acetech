from django.db import models

from django.db import models
from django.utils import timezone
import uuid

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Mobile Accessories', 'Mobile Accessories'),
        ('Computer Accessories', 'Computer Accessories'),
    ]

    STOCK_STATUS_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock'),
    ]

    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    dimensions = models.CharField(max_length=50, blank=True, null=True)
    stock_status = models.CharField(max_length=20, choices=STOCK_STATUS_CHOICES, default='In Stock')
    sold_count = models.PositiveIntegerField(default=0)
    watching_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    

class Cart(models.Model):
    session_id = models.CharField(max_length=255, db_index=True)  # Unique session for each visitor
    product_title = models.CharField(max_length=255)
    product_price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    delivery_option = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Generate a unique order number using UUID
            self.order_number = str(uuid.uuid4())[:8].upper()  # Shorten UUID to 8 characters
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} by {self.name}"
