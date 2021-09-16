from django.urls import path
from .views import UserWorkoutHomeView, TemplateEditView, TemplateDeleteView, TemplateCreateView
from . import views
from .models import Template

urlpatterns = [
    path('', UserWorkoutHomeView.as_view(), name='workout-home'),
    path('template/<int:pk>/edit/', TemplateEditView.as_view(), name='template-edit'),
    path('template/<int:pk>/delete/', TemplateDeleteView.as_view(), name='template-delete'),
    path('template/new', TemplateCreateView.as_view(), name='template-create'),
]
