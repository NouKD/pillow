from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions import Actions
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
# Register your models here.

#admin.site.register(models.SocialAccount)
#admin.site.register(models.SiteInfo)
#admin.site.register(models.Presentation)
#admin.site.register(models.Temoignage)

class SocialAccountAdmin(Actions):
    list_display =  ('nom','liens','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','liens','icone',]}),
        ("standare",{'fields':['status',]})
        ]


class SiteinfoAdmin(Actions):
    list_display =  ('date_add', 'date_update', 'status','logo_view')
    list_filter =  ('status',)
    date_hierarchy = 'date_add'
    list_per_page = 10
    readonly_fields = ['detail_logo']
    fieldsets = [
        ("infocategory",{'fields':['email','map_url','logo']}),
        ("standare",{'fields':['status',]})
        ]

    def logo_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.logo.url))

    def detail_logo(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.logo.url))            


class PresentationAdmin(Actions):
    list_display =  ('nom','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    readonly_fields = ['detail_image']
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','video','description','image']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    
    
    def detail_image(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))     


class TemoignageAdmin(Actions):
    list_display =  ('nom','prenom','date_add', 'date_update', 'status','photo_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    readonly_fields = ['detail_photo']
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','prenom','messages','photo']}),
        ("standare",{'fields':['status',]})
        ]

    def photo_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.photo.url))    
    
    def detail_photo(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.photo.url))    


class UserAccountInline(admin.StackedInline):
    model = models.UserAccount
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [UserAccountInline]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


admin.site.unregister(User)
_register(models.SocialAccount, SocialAccountAdmin)
_register(models.Presentation, PresentationAdmin)
_register(models.SiteInfo, SiteinfoAdmin)
_register(models.Temoignage, TemoignageAdmin)
_register(User, UserAdmin)
admin.site.register(models.OtherInfo)