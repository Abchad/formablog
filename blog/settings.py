import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# settings.py
DEFAULT_CHARSET = 'utf-8'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# --- Paramètres de base ---
# DEBUG : TOUJOURS FALSE EN PRODUCTION !
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True' # Charge DEBUG depuis une variable d'environnement

# ALLOWED_HOSTS : Les noms de domaine autorisés pour servir votre application
# Charge depuis une variable d'environnement, ou par défaut à une liste vide si non définie (sécurisé)
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
# Exemple pour le développement local, si non en DEBUG:
if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1'] + ALLOWED_HOSTS # Ajoute les hôtes de développement si en mode DEBUG


# SECRET_KEY : TRÈS IMPORTANT. Ne laissez JAMAIS votre clé secrète dans le code.
# Charge depuis une variable d'environnement. Si non définie, lève une erreur (nécessaire en production).
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    raise ImproperlyConfigured("La variable d'environnement DJANGO_SECRET_KEY n'est pas définie.")



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',  # On rajoute le nom de l'application
    'core', # Ajoutez cette ligne pour votre nouvelle application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Ajoutez le chemin vers votre dossier 'templates' à la racine du projet
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True, # Laisse Django chercher aussi dans les dossiers 'templates' des applications
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Ajoutez cette ligne pour définir la page de redirection après une connexion réussie
# Redirige vers la page d'accueil de votre blog après connexion
LOGIN_REDIRECT_URL = '/blog/'

# Vous pouvez également spécifier la page de connexion si elle n'est pas par défaut
# LOGIN_URL = '/accounts/login/'


WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# --- Base de Données (PostgreSQL) ---
# Charge les informations de la base de données depuis des variables d'environnement
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'), # L'hôte de votre DB sur Planethoster
        'PORT': os.environ.get('DB_PORT', '5432'), # Le port de votre DB sur Planethoster
        'OPTIONS': {
            'options': '-c client_encoding=utf8'
        }
    }
}

# --- Configuration Email (pour les formulaires de contact, réinitialisation de mot de passe, etc.) ---
# Charge les paramètres d'envoi d'emails depuis des variables d'environnement
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # Reste la même
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587)) # Par défaut à 587 (TLS)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'webmaster@votredomaine.com')




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# --- Fichiers Statiques ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Le dossier où les fichiers statiques seront collectés


# --- Médias (si vous en avez) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Paramètres de Sécurité supplémentaires (déjà mentionnés, à activer en production) ---
# Ces paramètres DOIVENT être activés quand HTTPS est configuré sur votre serveur !
# Ajoutez-les si ce n'est pas déjà fait et si vous êtes prêt pour HTTPS.
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False') == 'True'
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', 'False') == 'True'
# Pour HSTS (HTTP Strict Transport Security), à configurer APRES un premier déploiement HTTPS stable
# SECURE_HSTS_SECONDS = 31536000 # 1 an
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True


# --- Journalisation (Logging) ---
# Configurez la journalisation pour enregistrer les erreurs en production.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_errors.log'), # Chemin vers votre fichier de logs
        },
        'console': { # Ajout d'un handler console pour le développement
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'] if DEBUG else ['file'], # Envoie les logs à la console en dev
            'level': 'INFO' if DEBUG else 'ERROR', # Plus verbeux en dev
            'propagate': True,
        },
    },
}

# Nécessaire pour la vérification de SECRET_KEY si elle n'est pas définie
from django.core.exceptions import ImproperlyConfigured

