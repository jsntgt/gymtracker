from django.shortcuts import render, get_object_or_404
from .models import Template
from django.views.generic import ListView
from django.contrib.auth.models import User


class UserWorkoutHomeView(ListView):
    model = Template
    template_name = 'workout/workout_home.html'
    context_object_name = 'templates'
    ordering = ['name']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Template.objects.filter(author=user).order_by('name')
