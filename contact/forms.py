from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nome")
    phone = forms.CharField(label="Telefone")
    email = forms.EmailField(label="E-mail")
    message = forms.CharField(label="Mensagem", widget=forms.Textarea(attrs={'name':'body', 'rows':'3', 'cols':'5'}))