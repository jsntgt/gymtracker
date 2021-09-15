from django.urls import path
from .views import UserWorkoutHomeView, TemplateEditView
from . import views
from .models import Template

urlpatterns = [
    path('', UserWorkoutHomeView.as_view(), name='workout-home'),
    path('template/<int:pk>/edit/', TemplateEditView.as_view(), name='template-edit'),
]
