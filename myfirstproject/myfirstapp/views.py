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

def MyFirstPage(request):
    return render(request, "index.html")

def MySecondPage(request):
    return render(request, "second.html")

def MyThirdPage(request):
    Var = "My name is PEYMAN"
    Fruits = ["banana", "pineapple", "apple"]
    Num1, Num2 = 1, 3
    Ans = Num1 > Num2
    mydictionary = {
        "var": Var,
        "fruits": Fruits,
        "num1": Num1,
        "num2": Num2,
        "ans": Ans
    }
    # Context should be a dictionary
    return render(request, "third.html", context = mydictionary)

def MyImagePage1(request):
    return render(request, "imagepage1.html")

def MyImagePage2(request, imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    if myimagename == "django":
        Var = True
    elif myimagename == "python":
        Var = False
    mydictionary = {
        "var": Var
    }
    return render(request, "imagepage2.html", context = mydictionary) 