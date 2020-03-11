from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.SocialAccount)
admin.site.register(models.SiteInfo)
admin.site.register(models.Presentation)
admin.site.register(models.Temoignage)