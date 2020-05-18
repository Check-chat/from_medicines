from django.db import models
from noti_Prescription.models import Prescription

# Create your models here.

class remider(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)