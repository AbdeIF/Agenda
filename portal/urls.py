from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/add/', views.contato_add, name='contato_add'),
    path('contato/edit/<int:pk>/', views.contato_edit, name='contato_edit'),
    path('contato/delete/<int:pk>/', views.contato_delete, name='contato_delete')
]
