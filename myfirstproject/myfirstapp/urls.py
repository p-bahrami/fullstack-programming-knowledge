from django.urls import path
from .views import Index, About, Add, Intro, MyFirstPage, MySecondPage, MyThirdPage, MyImagePage1, MyImagePage2

urlpatterns = [
    path("", Index),
    path("about", About),
    path("add/<int:a>/<int:b>", Add),
    path("intro/<str:name>/<int:age>", Intro),
    path("myfirstpage", MyFirstPage),
    path("mysecondpage", MySecondPage),
    path("mythirdpage", MyThirdPage),
    path("myimagepage1", MyImagePage1),
    path("myimagepage2/<str:imagename>", MyImagePage2)
]
