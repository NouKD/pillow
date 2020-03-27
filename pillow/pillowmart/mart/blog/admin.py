from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions import Actions

# Register your models here.


#admin.site.register(models.CategorieArticle)
#admin.site.register(models.Tag)
#admin.site.register(models.Article)
#admin.site.register(models.Commentaire)


class ArticleAdmin(Actions):
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
    readonly_fields = ['detail_image']

    def image_view(self,obj):
        return mark_safe("<img src = '{url}'/ width='100px' height='50px'>".format(url=obj.image.url))    
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}/" width ="100px" height ="50px">'.format(url = obj.image.url))

class ArticleInline(admin.TabularInline):
    model = models.CategorieArticle
    extra = 0

class CategorieArticleAdmin(Actions):
    list_display =  ('nom','date_add', 'date_update', 'status','image_view')
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    readonly_fields = ['detail_image']
    inlines = [
        ArticleInline,
    ]
    fieldsets = [
        ("infocategory",{'fields':['nom','image','description']}),
        ("standare",{'fields':['status',]})
        ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))

    def detail_image(self,obj):
        return mark_safe("<img src='{url}'/ width='100px' height='50px'>".format(url=obj.image.url))        


class TagAdmin(Actions):
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





class CommentaireAdmin(Actions):
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


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.CategorieArticle, CategorieArticleAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
