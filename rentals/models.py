from django.db import models
from django.urls import reverse

class Color(models.Model):
    COLOR_CHOICES =[("BL", "Black"),
                    ("WH", "White"),
                    ("GY", "Gray"),
                    ("BR", "Browns"),
                    ("GR", "Green"),
                    ("BU", "Blue"),
                    ("PU", "Purple"),
                    ("RE", "Red"),
                    ("OR", "Orange"),
                    ("YE", "Yellow"),
    ]
    color = models.CharField(max_length=2, choices = COLOR_CHOICES, null = True, blank = True)


class Theme(models.Model):
    # ex. fancy beach floral
    THEME_CHOICES =[("NE", "Neon"),
                    ("BW", "Black & White"),
                    ("CR", "Carnival"),
                    ("DS", "Disco"),
                    ("SR", "Soirées"),
                    ("CK", "Cocktail"),
                    ("SH", "Showers"),
                    ("PP", "Pool Parties"),
                    ("FR", "Farewell"),
                    ("OD", "Outdoor"),
                    ("FN", "Fancy"),

    ]
    theme = models.CharField(max_length=2, choices = THEME_CHOICES, null = True, blank = True)


class Product(models.Model):
    CATEGORY_CHOICES =[ ("TB", "Tables"),
                        ("CH", "Chairs"),
                        ("GZ", "Arches & Gazebos"),
                        ("TN", "Tents"),
                        ("TA", "Tent Accessories"),
                        ("ST", "Stages"),
                        ("PR", "Projectors & Screens"),
                        ("EF", "Special Effects Equipments"),
                        ("AU", "Audio Systems"),
                        ("LT", "Lighting"),
                        ("LN", "Lenin"),
                        ("HN", "Hangers"),
                        ("GL", "Glasses & Stemware"),
                        ("FO", "Fun Food Equip"),
                        ("FL", "Floral Accessories"),
                        ("CR", "Floors & Carpet"),
                        ("TR", "Serving Trays"),
                        ("WR", "Flatware"),

    ]

    name = models.CharField(max_length = 50)
    img = models.ImageField(null=True, blank=True)
    measures = models.CharField(max_length = 50, null = True, blank = True)
    #quantity = models.IntegerField(null=True)
    description = models.TextField(null = True, blank = True)
    price_per_day = models.FloatField()
    is_available = models.BooleanField(default= True)
    category = models.CharField(max_length=2, choices = CATEGORY_CHOICES)
    #color = models.ManyToManyField(Color, null = True, blank = True)
    #theme = models.ManyToManyField(Theme, null = True, blank = True)


    def __str__(self):
        return "{} {} - ${}/day".format(self.name, self.measures, self.price_per_day)

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'product_id':self.id})
