from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_login, name='studmod1.html'),
    # Define other URLs as needed
]
