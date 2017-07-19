from django import forms
from models import UserModel

class SignUpForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['email', 'username', 'full_name', 'password']



class LoginForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['username', 'password']