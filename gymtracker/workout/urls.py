from django.urls import path
from .views import UserWorkoutHomeView
from . import views

urlpatterns = [
    path('', UserWorkoutHomeView.as_view(), name='workout-home'),
]
