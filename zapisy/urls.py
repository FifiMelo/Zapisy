from . import views
from django.urls import path

urlpatterns = [
    path('logout/', views.logout),
    path('login/', views.login),
    path('thanks/', views.thanks),
    path('user_panel/', views.user_panel),
    path('zapisy=<lan>/', views.zapisy),
    path('wypis/', views.wypis),
    path('', views.not_found)
]
