from django.urls import path,include
from panel import views

urlpatterns = [
        path('', views.home, name="home"),
        path('ourteamlist/', include('panel.ourteam.urls')),
        path('orderlist/', include('panel.order.urls')),
        path('book-online/', include('panel.book_online.urls')),

        ]
