from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions import Actions
# Register your models here.

#admin.site.register(models.Categorie)
#admin.site.register(models.Produit)

class ProduitAdmin(Actions):
    list_display =  ('nom','prix','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    readonly_fields = ['detail_image']
    fieldsets = [
        ("infocategory",{'fields':['nom','description','prix','image','categorie']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    

    def detail_image(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    

class ProduitInline(admin.TabularInline):
    model = models.Produit
    extra = 0

class CategorieAdmin(Actions):
    list_display =  ('nom','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    inlines = [
        ProduitInline,
    ]
    fieldsets = [
        ("infocategory",{'fields':['nom','description','image']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Categorie, CategorieAdmin)
_register(models.Produit, ProduitAdmin)




