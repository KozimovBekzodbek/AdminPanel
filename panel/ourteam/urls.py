from django.urls import path
from panel.ourteam import views

urlpatterns = [
        path('', views.OurTeamList, name="ourteamlist"),
        path('create/', views.OurTeamCreate, name="ourteamcreate"),
        path('update/<int:pk>', views.OurTeamUpdate, name="ourteamupdate"),
        path('delete/<int:pk>', views.OurTeamDelete, name="ourteamdelete"),

        ]
