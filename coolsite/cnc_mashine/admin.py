from django.contrib import admin

from .models import *

class CncListMetallAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'work_pole', 'emitter_type', 'power_laser', 'dimensions')
    list_display_links = ('id', 'model')
    search_fields = ('model',)
    prepopulated_fields = {'slug': ('model',)}

admin.site.register(CncListMetall, CncListMetallAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
