
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    nome_full = models.CharField(
        "Nome", max_length=100, blank=False, null=False)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'nome_full'
        'is_staff'
    ]

    def __str__(self):
        return self.email

    objects = UsuarioManager()


class Itens(models.Model):
    nome = models.CharField("Nome", null=False, max_length=200, blank=False)

    def __str__(self):
        return self.nome


class Solicitacao(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="solicitacao_user")
    solicitacao_itens = models.ManyToManyField(Itens)
    nome = models.CharField("Nome", null=False, max_length=200, blank=False)
    data_criacao = models.DateField("Data de Criação", auto_now_add=True)
    nif = models.CharField("NIF", max_length=9)
    observacao = models.CharField("Observação", max_length=200, blank=True)
    is_finalizado = models.BooleanField("Finalizado ou  em analise", default=False)

    def __str__(self):
        return self.nome
