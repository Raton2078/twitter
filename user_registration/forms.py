from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models  import CustomUser

#Création du formulaire personalisé permettant l'enregistrement de nouvels utilisateur
class SignUpForm(UserCreationForm):
        
        #Permet de personaliser le texte de l'aide de mots de passes 
        password1 = forms.CharField(
            label="Mot de passe",
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'}),
            help_text=""  # Supprime le texte d'aide
        )

        password2 = forms.CharField(
            label="Confirmez le mot de passe",
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez votre mot de passe'}),
            help_text=""  # Supprime le texte d'aide
        )
    	#Class permettant de modiier les éléments de la classe User/AbstractUser de Django
        class Meta:
            model = CustomUser  
            fields=['username', 'email','bio','password1', 'password2']
            widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre pseudo'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}),
                'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Parlez de vous...'}),

            }
            help_texts = {
                  'username': '',

            }
    
