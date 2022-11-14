from django import forms

from CalorieCounter.core.models import Motivation


class MotivationsCreateForm(forms.ModelForm):
    class Meta:
        model = Motivation
        fields = '__all__'
        labels = {
            'quote': 'Main text:',
            'description': 'Description:',
        }
