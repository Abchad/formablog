# C:\blog_django\src\posts\admin.py

from django.contrib import admin
from .models import BlogPost, Comment

# Enregistrer le modèle BlogPost
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on', 'updated_on')
    list_filter = ('status', 'created_on', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # Prérègle le slug à partir du titre
    raw_id_fields = ('author',) # Permet de rechercher l'auteur par ID
    date_hierarchy = 'created_on'
    ordering = ('status', '-created_on') # Trie par statut puis date

    # Actions personnalisées (exemple: publier/dépublier un article)
    actions = ['make_published', 'make_draft']

    def make_published(self, request, queryset):
        queryset.update(status=1)
        self.message_user(request, "Les articles sélectionnés ont été publiés avec succès.")
    make_published.short_description = "Publier les articles sélectionnés"

    def make_draft(self, request, queryset):
        queryset.update(status=0)
        self.message_user(request, "Les articles sélectionnés ont été mis en brouillon.")
    make_draft.short_description = "Mettre les articles sélectionnés en brouillon"


# Enregistrer le modèle Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, "Les commentaires sélectionnés ont été approuvés.")
    approve_comments.short_description = "Approuver les commentaires sélectionnés"

    def disapprove_comments(self, request, queryset):
        queryset.update(active=False)
        self.message_user(request, "Les commentaires sélectionnés ont été désapprouvés.")
    disapprove_comments.short_description = "Désapprouver les commentaires sélectionnés"

