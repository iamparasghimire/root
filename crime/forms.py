from django import forms
from .models import Crime

class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = '__all__'  # Use all fields from the Crime model
