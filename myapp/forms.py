from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','phno','message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phno': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }