from django.contrib import admin
from models import *

class ToolsAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SelectionAdmin(admin.ModelAdmin):
    list_display = ('toolname','selection')

class TopicsAdmin(admin.ModelAdmin):
    list_display = ('toolname',)

admin.site.register(Tools,ToolsAdmin)
admin.site.register(Community_Size, SelectionAdmin)
admin.site.register(Assessment_Focus, SelectionAdmin)
admin.site.register(Audience, SelectionAdmin)
admin.site.register(Topics, TopicsAdmin)