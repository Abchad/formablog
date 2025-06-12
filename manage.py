#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# C:\blog_django\src\manage.py
import os
import sys
from dotenv import load_dotenv # Nouvelle importation

def main():
    """Run administrative tasks."""
    # Charger les variables d'environnement du fichier .env
    load_dotenv() # Placez ceci au début de main()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

