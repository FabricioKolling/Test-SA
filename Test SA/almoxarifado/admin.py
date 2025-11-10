from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo', 'categoria', 'data']
    search_fields = ['categoria']
    list_filter = ['categoria']


admin.site.register(Item, ItemAdmin)