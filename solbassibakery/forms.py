from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True , min_length=4 , max_length=50,
                               widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id': 'username',
                                'placeholder':'Juan Rinaldi'
                               }))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'id': 'email',
                                'placeholder':'ejample@gmail.com'
                               }))
    password = forms.CharField(required=True , min_length=8 , max_length=20,
                               widget=forms.PasswordInput(attrs={
                                'class':'form-control',
                                'id': 'password',
                                'placeholder':'contraseña1234'
                               }))
    
    password2 = forms.CharField(label='confirmar password', required=True , min_length=8 , max_length=20,
                               widget=forms.PasswordInput(attrs={
                                'class':'form-control',
                                'id': 'password',
                                'placeholder':'contraseña1234'
                               }))
    


    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username
            
        

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email
        
    def clean(self):
        cleand_data = super().clean()
        if cleand_data.get('password2') != cleand_data.get('password'):
            self.add_error('password2', 'El password no coincide')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
                                  
        )
