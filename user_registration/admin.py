from django.contrib import admin
from .models import CustomUser  # Importer ton modèle utilisateur

admin.site.register(CustomUser)  # Enregistrer le modèle dans l’admin
