from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

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


def MyFormPage(request):
    return render(request, "myform.html")

def SubmitMyForm(request):
    mydictionary = {
        "var1": request.POST["mytext2"],
        "var2": request.POST["mytext4"],
        "meth": request.method
    }
    return JsonResponse(mydictionary)

def AddPage(request):
    return render(request, "adding.html")

def Result(request):
    var1 = int(request.GET['add1'])
    var2 = int(request.GET['add2'])
    res = var1 + var2
    return render(request, "result.html", {'result3': res})

def MyFormPage2(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = FeedbackForm(request.GET)
        if form.is_valid():
            title1 = request.GET['title']
            var = str("Form submitted" + str(title1) + str(request.method))
            return HttpResponse(var)
        else:
            mydictionary = {
             "form": form
            }
            return render(request, "myform2.html", context= mydictionary)


