from django.db import models
from django.contrib.auth import get_user_model

class Building(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    build_date = models.DateField()
    height = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name