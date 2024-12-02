from django import forms
from .models import Usuario, Libro, Review

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'publicado']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['usuario', 'libro', 'comentario', 'calificacion']
