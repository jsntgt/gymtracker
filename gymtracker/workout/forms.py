from django import forms
from django.contrib.auth.models import User
from .models import Template


class TemplateEditForm(forms.ModelForm):

    class Meta:
        model = Template
        fields = ['name', 'notes', 'exercises']
