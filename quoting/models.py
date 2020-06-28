from django.db import models

class CustomProduct(models.Model):
    length = models.IntegerField(blank=False, null=False)
    width = models.IntegerField(blank=False, null=False)
    height = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=254, blank=False, null=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.price
