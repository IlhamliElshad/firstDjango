from django.shortcuts import render,HttpResponse

# Create your views here.

def book(request):
    context = {
        "user1": "imran",
        "user2": "elshad",
        "user3": "orxan",
        "user4": "ilkin"
        
    }
    return render(request,"index.html",context)