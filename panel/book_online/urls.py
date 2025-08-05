from django.urls import path
from panel.book_online import views

urlpatterns = [
        path('', views.BookOnlineList, name="book-online"),
        path('create/', views.BookOnlineCreate, name="book-online-create"),
        path('update/<int:pk>', views.BookOnlineUpdate, name="book-online-update"),
        path('delete/<int:pk>', views.BookOnlineDelete, name="book-online-delete"),

        ]
