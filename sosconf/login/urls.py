from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.auth, name='index'),
    path('index/', views.auth),
    path('success', views.success),
]
