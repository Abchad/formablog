"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
# C:\blog_django\src\blog\wsgi.py
import os
from dotenv import load_dotenv # Nouvelle importation
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
# Charger les variables d'environnement du fichier .env
load_dotenv() # Placez ceci avant get_wsgi_application()

application = get_wsgi_application()