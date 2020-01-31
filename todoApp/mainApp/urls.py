from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('test_data/', views.send_testGraphData)
]
