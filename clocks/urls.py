from django.urls import path

from . import views

urlpatterns = [
    path('clocks/', views.ClocksView, name='clocks'),
    path('post/new', views.post_new, name='post_new'),
]