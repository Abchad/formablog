# C:\blog_django\src\blog\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Nouvelle page d'accueil à la racine du site
    path('', include('core.urls')), # Inclut les URLs de l'application 'core' à la racine

    # Toutes les URLs du blog (articles, création, édition, etc.) sous le préfixe 'blog/'
    path('blog/', include('posts.urls')),

    # Inclut les URLs d'authentification de Django (login, logout, password_change, reset)
    # Assurez-vous d'avoir des templates pour ces vues dans un dossier 'registration/' ou 'accounts/'
    # Par exemple: templates/registration/login.html
    path('accounts/', include('django.contrib.auth.urls')),
]
