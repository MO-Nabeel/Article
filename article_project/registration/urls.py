from django.urls import path
from articles import urls
from .import views


urlpatterns = [
    path("",views.reg,name="reg"),
    path("login",views.login,name="login"),
]