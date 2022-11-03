from django.db import models
class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.CharField(max_length=50, default="0")
    location = models.CharField(max_length=50, default= None)
    status = models.CharField(max_length=50, default= None)

    def __str__(self):
        return self.make + ' ' + self.carmodel + ' ' + self.year + ' ' + self.location + ' ' + self.status


    def is_rented(self):
        self.status == {"status":"booked"}
        return self.make + ' ' + self.carmodel + ' ' + self.year + ' ' + self.location + ' ' + self.status




class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    cars = models.CharField(max_length=1, default=0)


    def __str__(self):
        return self.name + ' ' + self.age + ' ' + self.address

    def rent_car(self):
        if self.cars == 0:
            return self.cars + 1
        else:
            return ("customer is allready renting a car")



class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.address + ' ' + self.branch