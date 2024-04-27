from django.db import models

class RealEstateObject(models.Model):
    cad_num = models.CharField()
    shirota = models.CharField()
    dolgota = models.CharField()