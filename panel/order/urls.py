from django.urls import path
from panel.order.views import OrderList, OrderCreate, OrderUpdate, OrderDelete



urlpatterns = [
        path('', OrderList, name = "order-list"),
        path('create/', OrderCreate, name = "order-create"),
        path('update/<int:pk>', OrderUpdate, name = "order-update"),
        path('delete/<int:pk>', OrderDelete, name = "order-delete"),

        ]
