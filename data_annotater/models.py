from django.db import models

# Create your models here.

#Schema
#Raw Fields
# merchant(text)
# sku(text)
# country(text,ISO)
#Annotation Fields
# retailer(text)
# segment(Choice: First Party, Third Party)

class StoreRecord(models.Model):
    merchant = models.CharField(max_length=50)
    sku = models.CharField(max_length=200)
    country = models.CharField(max_length=3)
    retailer = models.CharField(max_length=50, blank = True)
    segment = models.CharField(max_length=50, choices=[
        ('Third Party','Third Party'),
        ('First Party','First Party'),
    ], default='')

    # For better usability in Admin Console
    def __str__(self):
        return self.merchant