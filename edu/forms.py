from django import forms
from .models import Editora, Livro, Autor
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'publicacao': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'editora': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def clean_publicacao(self):
        publicacao = self.cleaned_data.get('publicacao')
        if publicacao and publicacao > timezone.now():
            raise forms.ValidationError('Essa data está no futuro')
        return publicacao


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'livros': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'email@exemplo.com', 'class': 'input-text'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Este email já está em uso.')
        return email


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input-text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'input-text'}))