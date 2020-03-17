from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

#admin.site.register(models.SocialAccount)
#admin.site.register(models.SiteInfo)
#admin.site.register(models.Presentation)
#admin.site.register(models.Temoignage)

class SocialAccountAdmin(admin.ModelAdmin):
    list_display =  ('nom','liens','icone','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','liens','icone','image']}),
        ("standare",{'fields':['status',]})
        ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.SocialAccount, SocialAccountAdmin)

class SiteinfoAdmin(admin.ModelAdmin):
    list_display =  ('email','date_add', 'date_update', 'status','logo_view')
    list_filter =  ('status',)
    date_hierarchy = 'date_add'
    list_display_links = ['email',]
    ordering = ['email',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['email','map_url','logo']}),
        ("standare",{'fields':['status',]})
        ]

    def logo_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.logo.url))    

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.SiteInfo, SiteinfoAdmin)

class PresentationAdmin(admin.ModelAdmin):
    list_display =  ('nom','video','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','video','description','video','image']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Presentation, PresentationAdmin)

class TemoignageAdmin(admin.ModelAdmin):
    list_display =  ('nom','prenom','date_add', 'date_update', 'status','photo_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','prenom','messages','photo']}),
        ("standare",{'fields':['status',]})
        ]

    def photo_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.photo.url))    

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Temoignage, TemoignageAdmin)