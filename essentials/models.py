from django.db import models

from django.db import models

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
