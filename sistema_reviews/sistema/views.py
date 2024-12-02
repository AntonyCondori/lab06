from django.shortcuts import render, redirect
from .forms import UsuarioForm, LibroForm, ReviewForm
from .models import Usuario, Libro, Review

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'sistema/crear_usuario.html', {'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_libro')
    else:
        form = LibroForm()
    return render(request, 'sistema/crear_libro.html', {'form': form})

def crear_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_review')
    else:
        form = ReviewForm()
    return render(request, 'sistema/crear_review.html', {'form': form})
