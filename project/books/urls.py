from django.urls import path
from books.views import book
urlpatterns = [
    path("",book)
]