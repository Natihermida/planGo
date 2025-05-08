from django import forms
from .models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['titulo', 'descripcion', 'fecha', 'imagen', 'plazas_disponibles']  # <--- aquí
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del plan'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del plan',
                'rows': 4
            }),
            'fecha': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'plazas_disponibles': forms.NumberInput(attrs={     # <--- estilo del input
                'class': 'form-control',
                'min': 1
            }),
        }
