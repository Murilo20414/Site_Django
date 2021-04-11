from django import forms 


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome: ', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome para contato'}))
    email = forms.EmailField(label='E-mail:', required=True, widget=forms.TextInput(attrs={'placeholder': 'Digite seu e-mail'}))
    message = forms.CharField(label='Mensagem:', required=True, widget=forms.Textarea(attrs={'placeholder': 'Escreva para nós...'}),)
