# C:\blog_django\src\core\forms.py

from django import forms

class ContactForm(forms.Form):
    """
    Formulaire de contact simple pour que les utilisateurs puissent envoyer un message aux administrateurs.
    """
    name = forms.CharField(max_length=100, label="Votre Nom")
    email = forms.EmailField(label="Votre Email")
    message = forms.CharField(widget=forms.Textarea, label="Votre Message")

