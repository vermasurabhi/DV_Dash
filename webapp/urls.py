from django.urls import path
from . import views
from .views import dataVisual
# from django.views.generic import TemplateView
from webapp.views import AboutView

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('basic/', dataVisual.as_view(), name='basic'),
    path('basic/<int:id>/', dataVisual.as_view()),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path("about/", AboutView.as_view()),
    path("map/", views.map, name="map"),
    path("datechart/", views.datechart,name="datechart"),
    path("experiment/", views.experiment,name="experiment"),
]

