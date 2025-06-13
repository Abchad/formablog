# C:\blog_django\src\blog\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('core.urls')), # Inclut les URLs de l'application 'core' à la racine (abchad.com/blog/)

    # Toutes les URLs du blog (articles, création, édition, etc.) sous le nouveau préfixe 'articles/'
    path('articles/', include('posts.urls')), # CHANGÉ ICI

    path('accounts/', include('django.contrib.auth.urls')),
]