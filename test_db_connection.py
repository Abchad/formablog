import psycopg2
import os

# Récupérez les informations de connexion de votre settings.py
DB_NAME = 'blog'
DB_USER = 'postgres'
DB_PASSWORD = 'abchad' # <--- IMPORTANT: METTEZ VOTRE VRAI MOT DE PASSE ICI (celui qui est dans settings.py)
DB_HOST = 'localhost'
DB_PORT = '5432'

try:
    # Tente de se connecter à la base de données
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Connexion à la base de données PostgreSQL réussie !")
    conn.close()
except psycopg2.Error as e:
    print(f"Erreur de connexion à la base de données : {e}")
    # Affiche la chaîne de connexion que psycopg2 a essayé d'utiliser
    print(f"DSN string that failed: {e.pgconn.dsn if e.pgconn else 'N/A'}")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")