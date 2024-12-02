from django.contrib import admin
from .models import Usuario, Libro, Review

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Review)