# C:\blog_django\src\core\urls.py

from django.urls import path
from .views import LandingPageView, ContactView # Nous allons créer ces vues

app_name = 'core' # Définir l'espace de noms pour cette application

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('contact/', ContactView.as_view(), name='contact'),
    # Vous pouvez ajouter d'autres URLs globales ici si nécessaire
]

