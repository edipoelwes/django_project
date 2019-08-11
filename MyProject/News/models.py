from django.db import models

# Create your models here.

class Novidades(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.autor

class Esporte(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()


    def __str__(self):
        return self.autor