from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class QuerySet(models.QuerySet):

    def promotor_nombres(self):
        return self.promotor_nombre

    def no_promovidos(self):
        return self.no_promovidos

class Promotor(models.Model):
    user = models.OneToOneField(User)
    nombre = models.CharField(max_length = 64)
    apellido = models.CharField(max_length = 64)
    no_promovidos = models.IntegerField()
    objects = QuerySet.as_manager()

    class Meta:
        permissions = (('puede_ser_promotor','puede_ser_promotor'),)
        ordering = ['user']


    def promovidos_limite(self):
        if self.no_promovidos <= 10:
            raise Exception("Solo puedes tener 10 promovidos")

    def __unicode__(self):
        return self.user.first_name

class Promovido(models.Model):
    promovido_id = models.IntegerField()
    promovido_nombre = models.CharField(max_length=64)
    promotor = models.ForeignKey(Promotor)
    voto = models.NullBooleanField()

    def __unicode__(self):
        return self.promovido_nombre
