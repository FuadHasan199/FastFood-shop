from django.db import models

# Create your models here.
class Pizaa(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4,decimal_places=2)
    priceL = models.DecimalField(max_digits=4,decimal_places=2)
    pImage = models.ImageField(upload_to='photos/pizaimage')

    def __str__(self):
        return self.name;

class Burger(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4,decimal_places = 2)
    priceL = models.DecimalField(max_digits=4,decimal_places=2)
    bImage = models.ImageField(upload_to='photos/burgerimage')

    def __str__(self):
        return self.name
    
class Drinks(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4,decimal_places=2)
    priceL = models.DecimalField(max_digits=4,decimal_places=2)
    dImage = models.ImageField(upload_to='photos/drinkimage')

    def __str__(self):
        return self.name