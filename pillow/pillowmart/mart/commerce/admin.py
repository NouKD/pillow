from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

#admin.site.register(models.Categorie)
#admin.site.register(models.Produit)

class CategorieAdmin(admin.ModelAdmin):
    list_display =  ('nom','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','description','image']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Categorie, CategorieAdmin)

class ProduitAdmin(admin.ModelAdmin):
    list_display =  ('nom','prix','categorie','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','description','prix','image','categorie']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Produit, ProduitAdmin)




