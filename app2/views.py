from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def home(request):
#     return HttpResponse("Welcome to the Home Page")

# def contact(request):
#     # return render(request, "<h1>Contact Us at: 1234567890</h1>")
#     return HttpResponse("<h1>Contact Us at: 1234567890</h1>")

def sign_up(request):
    return render(request, 'Registration/R1.html')

