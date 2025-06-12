# C:\blog_django\src\posts\urls.py
from django.urls import path
from .views import (
    BlogHome,
    BlogPostCreate,
    BlogPostDetail,
    BlogPostDelete,
    BlogPostEdit,
    # Vous pourriez ajouter une vue pour la publication d'articles ici si nécessaire
    # Par exemple, si les modérateurs doivent changer le statut de brouillon à publié
    # publish_blog_post_view # Une fonction/vue simple pour changer le statut
)

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('create/', BlogPostCreate.as_view(), name="create"),
    # VÉRIFIEZ CETTE LIGNE : le chemin pour l'édition
    path('<slug:slug>/edit/', BlogPostEdit.as_view(), name="edit"),
    path('<slug:slug>/delete/', BlogPostDelete.as_view(), name="delete"),
    path('<slug:slug>/', BlogPostDetail.as_view(), name="post"),
]