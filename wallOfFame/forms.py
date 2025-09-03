from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['photo', 'full_name', 'email', 'country', 'learning_track', 'linkedin', 'github']
