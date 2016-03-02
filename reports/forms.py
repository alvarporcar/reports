from django import forms

class FormLlistatAnual(forms.Form):
    Any = forms.CharField(max_length=4, label='Any')
    Projecte = forms.CharField(max_lenght=2,label='Projecte')
    
    