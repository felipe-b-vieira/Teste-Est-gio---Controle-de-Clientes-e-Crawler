from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator,MinLengthValidator
# Create your models here.


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(primary_key=True, max_length=11, validators=[RegexValidator(r'^\d{1,11}$'),MinLengthValidator(11)])
    rg = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$'),MinLengthValidator(9)])
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14, validators=[RegexValidator(r'^\d{1,9}$')])
    foto_perfil = models.ImageField(upload_to ='uploads/') 

#essas são as informações salvas pelo crawler
class RegistroGoogleCliente(models.Model):
	user = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	url = models.CharField(max_length=100)
	nomeLink = models.CharField(max_length=100)