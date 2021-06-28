from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('MyPage/',MyProfile,name="MyPage"),
    path('<int:pk>/edit/',edit,name="edit"),
]
