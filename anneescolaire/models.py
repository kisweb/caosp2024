from django.db import models

# Create your models here.

import datetime
from django.db import models

class AnneeScolaire(models.Model):
    
    annee = models.CharField(max_length=9, unique=True, db_index=True)
    statut = models.CharField(max_length=20, blank=True, default="AnneeEnCours")
    
    class Meta: 
        verbose_name = "AnneeScolaire"
        verbose_name_plural = "AnneeScolaires"

    def __str__(self):
        return self.annee
        
