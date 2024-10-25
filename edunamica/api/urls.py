from django.urls import path
from . import views

urlpatterns = [
    # URLs para Usuario
    path('usuarios/', views.UsuarioListCreate.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(), name='usuario-detail'),  

    #path('equipo_trabajo/')
]
