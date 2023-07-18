
from django.urls import path
from .views import home_view,get_rick_data_view

urlpatterns = [
    path("", home_view, name="home"),
    path("load/", get_rick_data_view, name="load"),
]
