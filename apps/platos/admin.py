from django.contrib import admin
from .models import Platos
# Register your models here.
@admin.register(Platos)
#admin.site.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio")
    list_filter = ("precio","nombre",)