from django.urls import path

from . import views

urlpatterns = [
    path('clocks/', views.ClocksView, name='clocks'),
]