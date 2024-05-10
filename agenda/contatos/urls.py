from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contatos, name='lista_contatos'),
    path('novo/', views.adicionar_contato, name='adicionar_contato'),
    path('editar/<int:pk>/', views.editar_contato, name='editar_contato'),
    path('deletar/<int:pk>/', views.deletar_contato, name='deletar_contato'),
]
