from django.contrib import admin
from game.models import Scene, Option

# custom model admins
class OptionInline(admin.TabularInline):
    model = Option
    extra = 3
    fk_name = 'scene'


class SceneAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Display', {'fields':['title', 'text']}),
    ]
    inlines = [OptionInline]

# Register your models here.
admin.site.register(Scene, SceneAdmin)
