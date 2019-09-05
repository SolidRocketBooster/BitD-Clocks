from django.urls import path

from . import views

urlpatterns = [
    path('clocks/', views.clocksView, name='clocks_list'),
    path('clocks/new', views.clockNew, name='clock_new'),
    path('clocks/<int:pk>/edit/', views.clockEdit, name='clocks_edit'),
    path('clocks/<int:pk>/delete/', views.clockDelete, name='clocks_delete'),
    path('clocks/<int:pk>/increase/', views.clockUp, name='clocks_up'),
    path('clocks/<int:pk>/decrease/', views.clockDown, name='clocks_down'),
]