from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Categorie)
admin.site.register(models.Produit)
