from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    plazas_disponibles = models.IntegerField(default=1)

    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planes_creados')
    participantes = models.ManyToManyField(User, related_name='planes_unidos', blank=True)
    imagen = models.ImageField(upload_to='planes_img/', blank=True, null=True)  # 👈 NUEVO

    def __str__(self):
        return self.titulo
