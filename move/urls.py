from django.urls import path
from . import views

urlpatterns = [
    path('forward/', views.move_forward),
    path('backward/', views.move_backward),
    path('boot/', views.boot)
]
