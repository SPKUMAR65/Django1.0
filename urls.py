from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/',views.deatils, name='detail'),
    path('', views.Course, name='home-page'),
]