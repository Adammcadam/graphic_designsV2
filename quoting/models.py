import uuid
from django.db import models

class CustomProduct(models.Model):
    unique_id = models.CharField(max_length=32, null=False, editable=False, default=0)
    length = models.IntegerField(blank=False, null=False)
    width = models.IntegerField(blank=False, null=False)
    height = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=254, blank=False, null=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.unique_id

    def _generate_unique_id(self):
        """
        Generate a random, unique id using UUID
        """
        return uuid.uuid4().hex.upper()

    def _update_price(self):
        price = (self.length * self.width * self.height) / 5000
        return price

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the unique id and price
        if it hasn't been set already.
        """
        if not self.unique_id:
            self.unique_id = self._generate_unique_id()
        if not self.price:
            self.price = self._update_price()
        super().save(*args, **kwargs)
