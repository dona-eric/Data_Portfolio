from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# formulaire de connexion de l'utilisateur

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length= 100, label='Nom utilisateur'
    )
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe",
               "class": 'form-control'}
               )
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        'class': "form-control"
    }))



# formulaire d'inscription

class InscriptionForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', "first_name", "last_name")



class AssistantForm(forms.Form):

    message = forms.CharField(max_length=500,
                              label='Posez-moi une question',
                              widget=forms.TextInput(
                                  attrs={"class":'form-control',
                                         'placeholder': 'Posez moi une question'
                                         }
                              ))
    