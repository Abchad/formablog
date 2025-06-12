# C:\blog_django\src\posts\views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages # Assurez-vous que messages est importé

from .models import BlogPost, Comment # Importez Comment
from .forms import BlogPostForm, CommentForm

class BlogHome(ListView):
    """
    Vue pour afficher la liste de tous les articles de blog.
    Les visiteurs peuvent consulter cette page.
    """
    model = BlogPost
    template_name = 'posts/blogpost_list.html'
    context_object_name = 'blog_posts'
    # N'afficher que les articles publiés pour les visiteurs
    # Pour les articles restreints, ils seront affichés, mais l'accès sera limité
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')


class BlogPostDetail(DetailView):
    """
    Vue pour afficher les détails d'un article de blog spécifique.
    Gère également l'accès aux articles restreints et les commentaires.
    """
    model = BlogPost
    template_name = 'posts/blogpost_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        qs = super().get_queryset()
        # Les superutilisateurs/modérateurs voient tous les articles (publiés ou brouillons)
        if self.request.user.is_authenticated and (self.request.user.is_superuser or self.request.user.groups.filter(name='Modérateurs').exists()):
            return qs
        # Les autres ne voient que les articles publiés
        return qs.filter(status=1)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.get_queryset()) # Utilise le queryset filtré
        
        # Logique pour les articles restreints
        if self.object.is_restricted and not request.user.is_authenticated:
            messages.warning(request, "Cet article est réservé aux utilisateurs connectés. Veuillez vous connecter ou vous inscrire.")
            # Redirige vers la page de connexion, en passant l'URL de l'article comme 'next'
            return redirect(reverse_lazy('login') + '?next=' + self.request.path)
            
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        # Commentaires actifs
        comments = post.comments.filter(active=True).order_by('created_on')
        context['comments'] = comments
        context['comment_count'] = comments.count()

        # Formulaire de commentaire
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Logique pour les articles restreints (empècher le commentaire si non connecté sur article restreint)
        if self.object.is_restricted and not request.user.is_authenticated:
            messages.error(request, "Vous devez être connecté pour commenter cet article restreint.")
            return redirect(reverse_lazy('login') + '?next=' + self.request.path)

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = self.object
            if request.user.is_authenticated:
                new_comment.author = request.user
                new_comment.name = request.user.username
                new_comment.email = request.user.email
            else:
                # Si l'utilisateur n'est pas connecté, s'assurer que les champs name et email sont remplis par le formulaire
                if not new_comment.name or not new_comment.email:
                     messages.error(request, "Veuillez fournir votre nom et email pour laisser un commentaire.")
                     context = self.get_context_data(**kwargs)
                     context['comment_form'] = comment_form
                     return self.render_to_response(context)


            new_comment.active = False # Les commentaires sont inactifs par défaut, en attente d'approbation
            new_comment.save()

            messages.success(request, 'Votre commentaire est en attente d\'approbation.')
            return redirect(self.object.get_absolute_url())
        else:
            context = self.get_context_data(**kwargs)
            context['comment_form'] = comment_form
            return self.render_to_response(context)


class BlogPostCreate(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'posts/blogpost_form.html'
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = 0 # Par défaut en brouillon
        return super().form_valid(form)

    def test_func(self):
        # Les superutilisateurs et les membres des groupes Contributeurs/Modérateurs peuvent créer
        return self.request.user.is_superuser or \
               self.request.user.groups.filter(name='Contributeurs').exists() or \
               self.request.user.groups.filter(name='Modérateurs').exists()


class BlogPostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'posts/blogpost_form.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('posts:post', kwargs={'slug': self.object.slug})

    def test_func(self):
        post = self.get_object()
        # L'utilisateur est l'auteur OU un modérateur/superutilisateur
        return self.request.user == post.author or \
               self.request.user.is_superuser or \
               self.request.user.groups.filter(name='Modérateurs').exists()


class BlogPostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'posts/blogpost_confirm_delete.html'
    success_url = reverse_lazy('posts:home')
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        # L'utilisateur est l'auteur OU un modérateur/superutilisateur
        return self.request.user == post.author or \
               self.request.user.is_superuser or \
               self.request.user.groups.filter(name='Modérateurs').exists()

