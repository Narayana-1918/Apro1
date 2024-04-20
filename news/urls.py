from django.urls import path
from .views import *

urlpatterns=[
    path('home/',home),
    path('sports/<int:id>',sports),
    path('politics/<int:id>',politics),
    path('cinema/<int:id>',cinema)



]