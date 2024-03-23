from .views import home
from django.urls import path

urlpatterns = [
    path('home/<int:id>', home, name="home")
]
