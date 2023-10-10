from django.urls import path
from .views import Index, About, Add, Intro

urlpatterns = [
    path("", Index),
    path("about", About),
    path("add/<int:a>/<int:b>", Add),
    path("intro/<str:name>/<int:age>", Intro)
]
