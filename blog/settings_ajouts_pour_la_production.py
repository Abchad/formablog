# C:\blog_django\src\blog\settings.py

# ... (votre configuration actuelle) ...

# 1. Désactiver le mode DEBUG
DEBUG = False # TRÈS IMPORTANT pour la production

# 2. Définir ALLOWED_HOSTS
# Remplacez 'yourdomain.com' par le nom de domaine de votre site en production
# ou par l'adresse IP de votre serveur.
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'localhost', '127.0.0.1']
# Si vous utilisez un serveur proxy, ajoutez aussi '0.0.0.0' si nécessaire,
# mais soyez spécifique avec vos hôtes.

# 3. Configuration des fichiers statiques pour la production
# C'est le répertoire où Django va collecter tous les fichiers statiques pour les servir
STATIC_ROOT = BASE_DIR / 'staticfiles' # Crée un dossier 'staticfiles' à la racine de votre projet src
STATIC_URL = '/static/'

# Vous devriez exécuter cette commande avant de déployer:
# python manage.py collectstatic

# 4. Clé secrète (SECRET_KEY)
# NE JAMAIS exposer votre SECRET_KEY en production.
# Utilisez une variable d'environnement ou un gestionnaire de secrets.
# Exemple avec une variable d'environnement:
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'votre-cle-secrete-par-defaut-non-securisee')
# En production, définissez la variable d'environnement DJANGO_SECRET_KEY avec une chaîne longue et aléatoire.

# 5. Base de données PostgreSQL
# Vous utilisez déjà PostgreSQL, ce qui est excellent pour la production.
# Assurez-vous que les identifiants (USER, PASSWORD, HOST, PORT) sont corrects pour votre serveur de base de données de production.
# Il est TRÈS recommandé d'utiliser des variables d'environnement pour ces informations sensibles.

# Exemple (non fonctionnel sans la config DB réelle, juste pour l'idée):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#     }
# }

# 6. Journalisation (Logging)
# Configurez la journalisation pour enregistrer les erreurs en production.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django_errors.log', # Chemin vers votre fichier de logs
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# 7. Autres paramètres de sécurité importants (Django les active par défaut ou avec quelques ajustements)
# SECURE_SSL_REDIRECT = True # Redirige toutes les requêtes HTTP vers HTTPS (nécessite HTTPS sur votre serveur)
# SESSION_COOKIE_SECURE = True # N'envoie le cookie de session que sur HTTPS
# CSRF_COOKIE_SECURE = True # N'envoie le cookie CSRF que sur HTTPS
# X_FRAME_OPTIONS = 'DENY' # Protège contre le "clickjacking" (déjà dans vos settings)
# SECURE_BROWSER_XSS_FILTER = True # Ajouté dans les versions récentes de Django

