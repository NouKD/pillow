from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.CategorieArticle)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.Commentaire)

class BlogAdmin(admin.modelAdmin):
    list_display
