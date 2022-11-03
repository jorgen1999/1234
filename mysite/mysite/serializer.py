from rest_framework import serializers
from .models import Car
from .models import Customer
from .models import Employee


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'carmodel', "year", "location", "status", "bookedBy"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'age', "address", "cars", "bookedCar"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'address', "branch"]