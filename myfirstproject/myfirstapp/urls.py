from django.urls import path
from .views import Index, About, Add, Intro, MyFirstPage, MySecondPage, MyThirdPage

urlpatterns = [
    path("", Index),
    path("about", About),
    path("add/<int:a>/<int:b>", Add),
    path("intro/<str:name>/<int:age>", Intro),
    path("myfirstpage", MyFirstPage),
    path("mysecondpage", MySecondPage),
    path("mythirdpage", MyThirdPage)
]
