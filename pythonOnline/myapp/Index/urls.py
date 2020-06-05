from django.urls import path
from .views import Home,BootTest,UserData

urlpatterns = [
    path('home/',Home,name='home'),
    path('bootstrap/',BootTest,name='bootstrap'),
    path('datacheck/',UserData,name="userdata")
]