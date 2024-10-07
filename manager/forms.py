from django import forms
from staff.models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'description', 'staff', 'is_complete', 'is_verified']
        widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter Task Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea', 
                'rows': 3, 
                'placeholder': 'Enter Task Description'
            }),
            'staff': forms.Select(attrs={
                'class': 'form-select'
            }),
            'is_complete': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
            'is_verified': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }