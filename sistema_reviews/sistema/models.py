from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    publicado = models.DateField()

    def __str__(self):
        return self.titulo

class Review(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.usuario} - {self.libro} - {self.calificacion}"