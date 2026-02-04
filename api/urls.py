from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios/', UsuarioListCreateAPIView.as_view()),
    path('usuarios/<int:pk>/', UsuarioUpdateDestroyAPIView.as_view()),
    path('users', listar_usuarios),
   
    path('imoveis/', ImovelListCreateAPIView.as_view()),
    path('imoveis/<int:pk>/', ImovelUpdateDestroyAPIView.as_view()),
    path('imoveis_list', listar_imoveis),
   
    path('contratos/', ContratoListCreateAPIView.as_view()),
    path('contratos/<int:pk>/', ContratoUpdateDestroyAPIView.as_view()),
    path('contratos_list', listar_contratos),
   
    path('pagamentos/', PagamentoListCreateAPIView.as_view()),
    path('pagamentos/<int:pk>/', PagamentoUpdateDestroyAPIView.as_view()),
    path('pagamentos_list', listar_pagamentos),
]
