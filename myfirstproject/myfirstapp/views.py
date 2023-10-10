from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def Index(request):
    return HttpResponse("Hello World!!")

def About(request):
    return HttpResponse("This is about section.")

def Add(request, a, b):
    return HttpResponse(a+b)

def Intro(request, name, age):
    mydictionary = {
        "name2": name,
        "age2": age
    }
    return JsonResponse(mydictionary)
