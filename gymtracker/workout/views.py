from django.shortcuts import render, get_object_or_404, redirect
from .models import Template, Exercise
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


def template_duplicate(request, pk):
    template = Template.objects.get(id=pk)
    exercises = template.exercises.all()
    template.id = None
    new_name = template.name + " - duplicate"
    if len(new_name) > 30:
        new_name = new_name[:30]
    template.name = new_name
    template.save()
    template.exercises.add(*exercises)
    template.save()
    return redirect('workout-home')


class UserWorkoutHomeView(ListView):
    model = Template
    template_name = 'workout/workout_home.html'
    context_object_name = 'templates'
    ordering = ['name']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Template.objects.filter(author=user).order_by('name')


class TemplateEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Template
    fields = ['name', 'notes', 'exercises']
    success_url = reverse_lazy('workout-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        template = self.get_object()
        if self.request.user == template.author:
            return True
        return False


class TemplateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Template
    success_url = reverse_lazy('workout-home')

    def test_func(self):
        template = self.get_object()
        if self.request.user == template.author:
            return True
        return False


class TemplateCreateView(LoginRequiredMixin, CreateView):
    model = Template
    fields = ['name', 'notes', 'exercises']
    success_url = reverse_lazy('workout-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
