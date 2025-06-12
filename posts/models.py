# C:\blog_django\src\posts\models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name="Auteur"
    )
    content = models.TextField(verbose_name="Contenu")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Dernière modification")

    STATUS_CHOICES = (
        (0, "Brouillon"),
        (1, "Publié"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="Statut")

    # Nouveau champ pour les articles restreints
    is_restricted = models.BooleanField(default=False, verbose_name="Accès restreint (nécessite connexion)")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article de blog"
        verbose_name_plural = "Articles de blog"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:post', kwargs={'slug': self.slug})

    @property
    def author_or_default(self):
        return self.author.username if self.author else "Auteur inconnu"


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Article"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_comments',
        null=True, blank=True,
        verbose_name="Utilisateur (si connecté)"
    )
    name = models.CharField(max_length=80, verbose_name="Nom (si anonyme)")
    email = models.EmailField(blank=True, verbose_name="Email (si anonyme)")
    body = models.TextField(verbose_name="Contenu du commentaire")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    active = models.BooleanField(default=False, verbose_name="Actif (approuvé)")

    class Meta:
        ordering = ['created_on']
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return f"Commentaire par {self.name} sur '{self.post.title}'"

