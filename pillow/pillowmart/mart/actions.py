from django.contrib import admin


class Actions(admin.ModelAdmin):
    actions = ('active', 'desactive',)

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'Activer')

    active.short_description = 'active '

    def desactive(self, queryset, request):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver')

    desactive.short_description = 'desactive'