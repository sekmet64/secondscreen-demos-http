from django.db import models


class ShortenedUrl(models.Model):
    PRODUCT_CHOICES = (
        ('Y', 'YouTube demo'),
        ('R', 'Remote mouse app')
    )

    uniqueId = models.CharField(max_length=10)
    associatedProduct = models.CharField(max_length=1, choices=PRODUCT_CHOICES)
