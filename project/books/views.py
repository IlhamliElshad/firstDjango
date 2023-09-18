from django.shortcuts import render,HttpResponse
from books.models import Book
# Create your views here.

def book(request):
    context = {
        "books":Book.objects.all() # butun bu modelin obyektlerini getirir
    }
    return render(request,"index.html",context)