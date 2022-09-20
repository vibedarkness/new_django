from django.contrib import admin

from django.utils.html import format_html

# Register your models here.

from .models import Candidat


class CandidatAdmin(admin.ModelAdmin):
    list_filter=['status']
    list_display= ['firstname','lastname','email','job','statusvibe','_','created_at']
    search_fields=['firstname','lastname','email','job','age','status']
    list_per_page: 10

    #fonction de changement d'etat

    def _(self,obj):
        if obj.status=="Approuver":
            return True
        elif obj.status=="Attente":
            return None
        else:
            return False

    _.boolean=True
    #fonction de changement de couleur

    def statusvibe(self,obj):
        if obj.status=="Approuver":
            color='green'
        elif obj.status=="Attente":
            color='#fea95e'
        else:
            color='red'

        return format_html('<stong><p style="color: {}">{}</p></strong>'.format(color,obj.status))

    statusvibe.allow_tags=True

admin.site.register(Candidat,CandidatAdmin)