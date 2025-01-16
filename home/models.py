# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Produtos(models.Model):

    #__Produtos_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)
    quantidade = models.CharField(max_length=255, null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)

    #__Produtos_FIELDS__END

    class Meta:
        verbose_name        = _("Produtos")
        verbose_name_plural = _("Produtos")


class Filial(models.Model):

    #__Filial_FIELDS__
    descricao = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)

    #__Filial_FIELDS__END

    class Meta:
        verbose_name        = _("Filial")
        verbose_name_plural = _("Filial")



#__MODELS__END
