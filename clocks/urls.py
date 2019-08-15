from django.urls import path

from . import views

urlpatterns = [
    path('clocks/', views.ClocksView, name='clocks_list'),
    path('clocks/new', views.postNew, name='clock_new'),
    path('clocks/<int:pk>/edit/', views.clockEdit, name='clocks_edit'),
    path('clocks/<int:pk>/delete/', views.clockDelete, name='clocks_delete'),
]