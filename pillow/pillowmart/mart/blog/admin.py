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
    actions = ('active', 'desactive',)

      def active(self, request, queryset):
          queryset.update(statut=True)
          self.message_user(request, 'Activer une Article')
      active.short_description = 'active Article'

      def desactive(self, queryset, request):
          queryset.update(statut = False)
          self.message_user(request, 'Desactiver une Article')
      desactive.short_description = 'desactive Article'

    def image_view(self,obj)
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    
    
class ArticleInline(admin.TabularInline):
    model = models.Catégorie
    extra = 0

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
    actions = ('active', 'desactive',)

      def active(self, request, queryset):
          queryset.update(statut=True)
          self.message_user(request, 'Activer une CategorieArticle')
      active.short_description = 'active CategorieArticle'

      def desactive(self, queryset, request):
          queryset.update(statut = False)
          self.message_user(request, 'Desactiver une CategorieArticle')
      desactive.short_description = 'desactive CategrieAticle '
    inlines = [
        ArticleInline,
    ]
    fieldsets = [
        ("infocategory",{'fields':['nom','image','description']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    

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
    actions = ('active', 'desactive',)

      def active(self, request, queryset):
          queryset.update(statut=True)
          self.message_user(request, 'Activer une Tag')
      active.short_description = 'active Tag'

      def desactive(self, queryset, request):
          queryset.update(statut = False)
          self.message_user(request, 'Desactiver une Tag')
      desactive.short_description = 'desactive Tag'
    fieldsets = [
        ("infocategory",{'fields':['nom','description']}),
        ("standare",{'fields':['status',]})
        ]

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
    actions = ('active', 'desactive',)

      def active(self, request, queryset):
          queryset.update(statut=True)
          self.message_user(request, 'Activer une Commentaire')
      active.short_description = 'active Commentaire'

      def desactive(self, queryset, request):
          queryset.update(statut = False)
          self.message_user(request, 'Desactiver une Commentaire')
      desactive.short_description = 'desactive Commentaire'
    fieldsets = [
        ("infocategory",{'fields':['nom','prenom','article','commentaire']}),
        ("standare",{'fields':['status',]})
        ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Commentaire, CommentaireAdmin)
