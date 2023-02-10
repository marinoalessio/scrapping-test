from django.db import models

# Create your models here.

class Boat(models.Model):
    title = models.CharField(max_length=120)
    price = models.CharField(max_length=60)

    def _str_title_(self):
        return self.title
    
    def _str_price_(self):
        return self.price
