from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions import Actions
# Register your models here.

#admin.site.register(models.Contact)
#admin.site.register(models.NewsLetter)

class ContactAdmin(Actions):
    list_display =  ('nom','sujet','date_add', 'date_update', 'status',)
    list_filter =  ('status',)
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom',]
    ordering = ['nom',]
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['nom','email','message','sujet',]}),
        ("standare",{'fields':['status',]})
        ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Contact, ContactAdmin)

class NewsLetterAdmin(Actions):
    list_display =  ('date_add', 'date_update','status')
    list_filter =  ('status',)
    date_hierarchy = 'date_add'
    list_per_page = 10
    fieldsets = [
        ("infocategory",{'fields':['email',]}),
        ("standare",{'fields':['status',]})
        ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.NewsLetter, NewsLetterAdmin)

