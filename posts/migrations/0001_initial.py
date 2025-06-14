# Generated by Django 2.2.28 on 2025-06-13 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('content', models.TextField(verbose_name='Contenu')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('status', models.IntegerField(choices=[(0, 'Brouillon'), (1, 'Publié')], default=0, verbose_name='Statut')),
                ('is_restricted', models.BooleanField(default=False, verbose_name='Accès restreint (nécessite connexion)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
            ],
            options={
                'verbose_name': 'Article de blog',
                'verbose_name_plural': 'Articles de blog',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nom (si anonyme)')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email (si anonyme)')),
                ('body', models.TextField(verbose_name='Contenu du commentaire')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('active', models.BooleanField(default=False, verbose_name='Actif (approuvé)')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur (si connecté)')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.BlogPost', verbose_name='Article')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
                'ordering': ['created_on'],
            },
        ),
    ]
