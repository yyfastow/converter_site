from django.db import models

# Create your models here.
class Shape(models.Model):
    shape = models.CharField(max_length=34)
    dimension = models.IntegerField(default=2)
    measurement = models.CharField(max_length=34, default='area')
    
    def __str__(self):
        return self.shape
    
    
