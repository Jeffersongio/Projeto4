import email
from django.db import models

class Pessoa(models.Model):
    Nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.IntegerField(max_length=20)