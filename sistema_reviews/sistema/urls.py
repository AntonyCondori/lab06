from django.urls import path
from . import views

urlpatterns = [
    path('usuario/crear/', views.crear_usuario, name='crear_usuario'),
    path('libro/crear/', views.crear_libro, name='crear_libro'),
    path('review/crear/', views.crear_review, name='crear_review'),
]
