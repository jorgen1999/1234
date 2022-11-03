from .models import Car
from .models import Customer
from .models import Employee
from .serializer import CustomerSerializer
from .serializer import EmployeeSerializer
from rest_framework.response import Response
from .serializer import CarSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view



@api_view(["GET"])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def update_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------------------------------------------
@api_view(["GET"])
def get_customer(request):
    cars = Customer.objects.all()
    serializer = CustomerSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def save_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def update_customer(request, id):
    try:
        theCar = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_customer(request, id):
    try:
        theCar = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#-----------------------------------------------------------------------

@api_view(["GET"])
def get_employee(request):
    cars = Employee.objects.all()
    serializer = EmployeeSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def save_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def update_employee(request, id):
    try:
        theCar = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EmployeeSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_employee(request, id):
    try:
        theCar = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def order_car (request, idCustomer, idCar):
    try:
        theCar = Car.objects.get(pk=idCar)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        theCustomer = Customer.objects.get(pk=idCustomer)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if theCar.status == "Booked" or theCustomer.cars != 0 or theCar.status == "Damaged":
        return Response(status=status.HTTP_404_NOT_FOUND)

    theCar.status = "Booked"
    theCustomer.cars += 1
    theCar.bookedBy = idCustomer
    theCustomer.bookedCar = idCar

    theCar.save()
    theCustomer.save()

    serializer = CarSerializer(theCar, data=request.data)
    serializer.save

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def cancel_car (request, idCustomer, idCar):
    try:
        theCar = Car.objects.get(pk=idCar)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        theCustomer = Customer.objects.get(pk=idCustomer)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if theCar.status == "Available" or theCustomer.cars != 1:
        return Response(status=status.HTTP_404_NOT_FOUND)

    theCar.status = "Available"
    theCustomer.cars -= 1
    theCar.bookedBy = 0
    theCustomer.bookedCar = 0

    theCar.save()
    theCustomer.save()

    serializer = CarSerializer(theCar, data=request.data)
    serializer.save

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def rent_car(request, idCustomer, idCar):
    try:
        theCar = Car.objects.get(pk=idCar)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        theCustomer = Customer.objects.get(pk=idCustomer)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if theCar.status != "Booked" or theCustomer.cars != 1 or theCar.bookedBy != idCustomer:
        return Response(status=status.HTTP_404_NOT_FOUND)

    theCar.status = "Rented"
    theCar.bookedBy = idCustomer
    theCustomer.bookedCar = idCar

    theCar.save()
    theCustomer.save()

    serializer = CarSerializer(theCar, data=request.data)
    serializer.save

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def return_car (request, idCustomer, idCar):
    try:
        theCar = Car.objects.get(pk=idCar)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        theCustomer = Customer.objects.get(pk=idCustomer)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if theCar.status != "Rented" or theCustomer.cars != 1 or theCar.bookedBy != idCustomer:
        return Response(status=status.HTTP_404_NOT_FOUND)

    theCar.status = "Available"
    theCustomer.cars = 0
    theCar.bookedBy = 0
    theCustomer.bookedCar = 0

    theCar.save()
    theCustomer.save()

    serializer = CarSerializer(theCar, data=request.data)
    serializer.save

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)





















