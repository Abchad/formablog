# C:\blog_django\src\posts\templatetags\posts_tags.py

from django import template
from django.contrib.auth.models import Group # Importe le modèle Group
# Vous pourriez avoir besoin d'importer BlogPost si vous passez l'objet post au filtre
# from ..models import BlogPost

register = template.Library() # Enregistre les filtres et balises pour Django

@register.filter(name='has_group')
def has_group(user, group_name):
    """
    Vérifie si un utilisateur appartient à un groupe donné.
    Utilisation dans les templates: {% if request.user|has_group:"NomDuGroupe" %}
    """
    if user.is_authenticated:
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return False
        return group in user.groups.all()
    return False # Un utilisateur non authentifié n'appartient à aucun groupe


@register.filter(name='can_add_article')
def can_add_article(user):
    """
    Vérifie si un utilisateur authentifié a le droit d'ajouter un nouvel article.
    (Superutilisateur ou membre des groupes 'Contributeurs' ou 'Modérateurs')
    """
    return user.is_authenticated and (
        user.is_superuser or
        user.groups.filter(name='Contributeurs').exists() or
        user.groups.filter(name='Modérateurs').exists()
    )


@register.filter(name='can_manage_article')
def can_manage_article(user, post):
    """
    Vérifie si un utilisateur authentifié peut éditer ou supprimer un article.
    (Auteur de l'article OU Superutilisateur OU membre du groupe 'Modérateurs')
    """
    if not user.is_authenticated:
        return False
    return user == post.author or \
           user.is_superuser or \
           user.groups.filter(name='Modérateurs').exists()


@register.filter(name='can_publish_article')
def can_publish_article(user, post):
    """
    Vérifie si un utilisateur authentifié peut publier un article (changer son statut de brouillon à publié).
    (Superutilisateur ou membre du groupe 'Modérateurs') et si l'article est en brouillon (status=0).
    """
    if not user.is_authenticated or post.status == 1: # Déjà publié ou utilisateur non connecté
        return False
    return user.is_superuser or user.groups.filter(name='Modérateurs').exists()

