# Smart AgroTech Sénégal — Backend

Backend Django REST Framework du projet Smart AgroTech Sénégal.

## Installation

1. Cloner le dépôt

git clone https://github.com/GYERFRV/smart-agrotech-senegal-backend.git
cd smart-agrotech-senegal-backend


2. Créer et activer l'environnement virtuel

python -m venv venv
venv\Scripts\activate


3. Installer les dépendances

pip install -r requirements.txt


4. Créer un fichier `.env` à la racine du projet avec :

SECRET_KEY=une_cle_secrete_a_generer
DEBUG=True
DB_NAME=smart_agrotech
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432


Pour générer une clé secrète :

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


5. Créer la base de données PostgreSQL
```sql
CREATE DATABASE smart_agrotech;
```

6. Appliquer les migrations

python manage.py migrate


7. Créer un compte administrateur

python manage.py createsuperuser


8. Lancer le serveur

python manage.py runserver


L'API est accessible sur `http://127.0.0.1:8000/`
