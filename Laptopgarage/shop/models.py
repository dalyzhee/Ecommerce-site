from django.db import models
from matplotlib import image

class Product(models.Model):
    title = models.CharField(max_length=100, default='Laptop')
    description = models.TextField()
    price = models.IntegerField()
    categories = models.ManyToManyField('Category', related_name='products')
    image = models.ImageField(upload_to='images/')
    sold_out = models.BooleanField(default=False)
    # added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=100, default="motherboard repair")
    image = models.ImageField(upload_to='images/service/')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, default='Laptop')

    def __str__(self):
        return self.name
