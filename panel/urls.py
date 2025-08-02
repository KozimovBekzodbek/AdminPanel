from django.urls import path,include
from panel import views

urlpatterns = [
        path('', views.home, name="home"),
        path('ourteamlist/', include('panel.ourteam.urls')),

        ]
