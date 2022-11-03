"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import get_cars
from .views import save_car
from .views import update_car
from .views import delete_car
from .views import get_customer
from .views import save_customer
from .views import delete_customer
from .views import update_customer
from .views import get_employee
from .views import save_employee
from .views import delete_employee
from .views import update_employee
from .views import order_car
from .views import cancel_car
from .views import rent_car
from .views import return_car


urlpatterns = [
 path("admin/", admin.site.urls),
 path("cars/", get_cars),
 path("save_car/", save_car),
 path("update_car/<int:id>", update_car),
 path("delete_car/<int:id>", delete_car),
 path("get_customer", get_customer),
 path("save_customer", save_customer),
 path("update_customer/<int:id>", update_customer),
 path("delete_customer/<int:id>", delete_customer),
 path("get_employee", get_employee),
 path("save_employee", save_employee),
 path("update_employee/<int:id>", update_employee),
 path("delete_employee/<int:id>", delete_employee),
 path("order_car/<int:id>", order_car),
 path("order_car/<int:idCustomer>-<int:idCar>", order_car),
 path("cancel_car/<int:idCustomer>-<int:idCar>", cancel_car),
 path("rent_car/<int:idCustomer>-<int:idCar>", rent_car),
 path("return_car/<int:idCustomer>-<int:idCar>", return_car)
]