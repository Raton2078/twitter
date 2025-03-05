from django import forms
from . import models


#Initialisation du formulaire afin de permettre aux utilisateur de poster
class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['content']