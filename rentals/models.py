from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 50)
    measures = models.CharField(max_length = 50)
    #color = models.
    description = models.TextField()
    price = models.FloatField()
    is_available = models.BooleanField(default= True)

    #type = chairs tables banners
    #theme = fancy beach floral
