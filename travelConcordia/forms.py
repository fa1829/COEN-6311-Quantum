# travelConcordia/forms.py
from django import forms
from .models import Agent

class AgentCreationForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
