from django.contrib import admin
from .models import CustomUser  # Importer ton modèle utilisateur

#Creation d'administrateur avec la classe définit plus tôt CustomUser
admin.site.register(CustomUser)  # Enregistrer le modèle dans l’admin
