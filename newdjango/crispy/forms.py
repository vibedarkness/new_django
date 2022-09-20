from django import forms
from django.core.validators import RegexValidator
from .models import Candidat


class CandidatForm(forms.ModelForm):

    # validations
    firstname = forms.CharField(label='Prenom', min_length=3, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': 'Prenom'}))
    lastname = forms.CharField(label='Nom', min_length=2, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    age = forms.CharField(label='Age', min_length=1, max_length=3, validators=[RegexValidator(
        r'^[0-9]*$', message='ce champ ne dois contenir que des entiers')], widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    email = forms.CharField(label='Email', min_length=5, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="ceci n'est pas un email valide")], widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    # phone = forms.CharField(label='Telephone' ,min_length=1, max_length=3, validators=[RegexValidator(r'^[0-9]*$', message='ce champ ne dois contenir que des entiers')], widget=forms.TextInput(attrs= {'placeholder':'Telephone'}))
    message = forms.CharField(label='Message', required=True, min_length=10, max_length=1000,
                              widget=forms.Textarea(attrs={'placeholder': 'Messages', 'rows': 10}))

    class Meta:
        model = Candidat
        fields = ['firstname', 'lastname', 'email', 'age', 'phone', 'message']
        widgets = {
            'phone': forms.TextInput(attrs={
                'style': 'font-size: 15px',
                'placeholder': 'Telephone',
                'data-mask':'(+000) 00-000-00-00'
                 })
        }
