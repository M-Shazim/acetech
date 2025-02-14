from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Mobile Accessories', 'Mobile Accessories'),
        ('Computer Accessories', 'Computer Accessories'),
    ]

    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
    

class Cart(models.Model):
    session_id = models.CharField(max_length=255, db_index=True)  # Unique session for each visitor
    product_title = models.CharField(max_length=255)
    product_price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
