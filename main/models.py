import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("shoes", "Shoes"),
        ("clothes", "Clothes"),          
        ("accessories", "Accessories"),
        ("limited", "Limited Edition"),
    ]

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="shoes"   
    )
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    dummy_field = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.name
