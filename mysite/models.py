from django.db import models
class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.make + ' ' + self.carmodel + ' ' + self.year + ' ' + self.location + ' ' + self.status
        
    
