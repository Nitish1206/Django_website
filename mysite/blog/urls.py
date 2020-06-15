
# This is blog url made by me

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome")
]

