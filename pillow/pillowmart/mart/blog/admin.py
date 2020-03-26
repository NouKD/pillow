from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


#admin.site.register(models.CategorieArticle)
#admin.site.register(models.Tag)
#admin.site.register(models.Article)
#admin.site.register(models.Commentaire)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("infocategory",{'fields':['titre','image','description','contenue','tag']}),
        ("standare",{'fields':['status',]})
        ]
    list_display =  ('titre','date_add', 'date_update', 'status','categorie','image_view')
    list_filter =  ('status',)
    search_fields = ('titre','categorie',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre',]
    ordering = ['titre',]
    filter_horizontal = ('tag',)
    list_per_page = 10

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    
    
class ArticleInline(admin.TabularInline):
    model = models.Catégorie
    extra = 0
    

    actions = ["activate" ,"deactivate"]

    def activate (self, request, queryset):
        queryset.update(status = True)
        self.message_user(request,"la sélection à été activé avec succès")
    deactive.short_description = 'Activer'
    def deactivate (self, request, queryset):
        queryset.update(status = False)
        self.message_user(request,"la sélection à été desactivé avec succès")
    active.short_description = 'Desactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Article, ArticleAdmin)


class CategorieArticleAdmin(admin.ModelAdmin):
    list_display =  ('nom','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    inlines = [
        ArticleInline,
    ]
    fieldsets = [
        ("infocategory",{'fields':['nom','image','description']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    

    actions = ["activate" ,"deactivate"]

    def activate (self, request, queryset):
        queryset.update(status = True)
        self.message_user(request,"la sélection à été activé avec succès")
    deactive.short_description = 'Activer'
    def deactivate (self, request, queryset):
        queryset.update(status = False)
        self.message_user(request,"la sélection à été desactivé avec succès")
    active.short_description = 'Desactiver'

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.CategorieArticle, CategorieArticleAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display =  ('nom','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','description']}),
        ("standare",{'fields':['status',]})
        ]
    #actions = ["activate" ,"deactivate"]
    def activate (self, request, queryset):
        queryset.update(status = True)
        self.message_user(request,"la sélection à été activé avec succès")
    deactive.short_description = 'Activer'
    def deactivate (self, request, queryset):
        queryset.update(status = False)
        self.message_user(request,"la sélection à été desactivé avec succès")
    active.short_description = 'Desactiver'


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Tag, TagAdmin)
class CommentaireAdmin(admin.ModelAdmin):
    list_display =  ('nom','article','prenom','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','prenom','article','commentaire']}),
        ("standare",{'fields':['status',]})
        ]

    actions = ["activate" ,"deactivate"]

    def activate (self, request, queryset):
        queryset.update(status = True)
        self.message_user(request,"la sélection à été activé avec succès")
    deactive.short_description = 'Activer'
    def deactivate (self, request, queryset):
        queryset.update(status = False)
        self.message_user(request,"la sélection à été desactivé avec succès")
    active.short_description = 'Desactiver'
    
def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Commentaire, CommentaireAdmin)
