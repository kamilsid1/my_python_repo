from .views import home
from django.urls import path

urlpatterns = [
    path('home/<str:ab>/<slug:pk>/<int:pkid>/<path:abid>', home, name="home")
]
