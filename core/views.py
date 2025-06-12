# C:\blog_django\src\core\views.py

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm # Nous allons créer ce formulaire

class LandingPageView(TemplateView):
    """
    Vue pour la nouvelle page d'accueil avec le menu principal.
    """
    template_name = 'core/landing_page.html'

class ContactView(FormView):
    """
    Vue pour la page de contact.
    Utilise un formulaire pour collecter les messages des utilisateurs.
    """
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:landing_page') # Redirection après envoi réussi

    def form_valid(self, form):
        # Ici, vous traiteriez l'envoi de l'email.
        # Pour le moment, nous allons juste afficher un message.
        # Exemple basique d'envoi d'email (nécessite une configuration email dans settings.py)
        # from django.core.mail import send_mail
        # send_mail(
        #     f"Nouveau message de contact de {form.cleaned_data['name']}",
        #     form.cleaned_data['message'],
        #     form.cleaned_data['email'],
        #     ['votre_email_admin@example.com'], # Remplacez par l'email de l'administrateur
        #     fail_silently=False,
        # )

        messages.success(self.request, 'Votre message a été envoyé avec succès aux administrateurs.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Veuillez corriger les erreurs dans le formulaire.')
        return super().form_invalid(form)

