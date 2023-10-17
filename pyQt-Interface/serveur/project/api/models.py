from django.db import models

class Dht11(models.Model) :
    data = models.CharField(max_length=20)
