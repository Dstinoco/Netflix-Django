from django.shortcuts import render

# Create your views here.
def homepage(request):
    return(request, 'homepage.html')