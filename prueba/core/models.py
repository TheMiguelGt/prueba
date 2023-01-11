from django.db import models

# Create your models here.
class ipGenerate(models.Model):
    valor = models.IntegerField(null=False,unique=True)
