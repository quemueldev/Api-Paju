from django.db import models
from django.contrib.auth.models import User

class Materia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materia')
    titulo = models.CharField(max_length=50)

class Assunto(models.Model):
    materia =  models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='assunto')
    titulo = models.CharField(max_length=50)

class Resumo(models.Model):
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE, related_name='resumo')
    titulo = models.CharField(max_length=50)
    texto = models.TextField()


class Perfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil"
    )
    bio = models.TextField(blank=True)
    #foto = models.ImageField(upload_to="perfil/", blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
