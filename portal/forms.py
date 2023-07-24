from django import forms

from portal.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': ' form-control', 'autofocus': ''}),
            'sobrenome': forms.TextInput(attrs={'class': ' form-control'}),
            'email': forms.EmailInput(attrs={'class': ' form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': ' form-control'}),
        }
