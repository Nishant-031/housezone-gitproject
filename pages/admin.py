from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnails(self, objects):
        return format_html('<img src= "{}" height= "40" style= "border-radius : 50px" />'.format(objects.image.url))

    thumbnails.short_description= 'Photo'

    list_display = ('id', 'thumbnails', 'first_name', 'last_name', 'designation', 'created_date', )
    list_display_links= ('thumbnails', 'first_name', 'last_name', 'designation', 'created_date', )
    search_fields= ('first_name', 'last_name', 'designation', )
    list_filter= ('designation', )


admin.site.register(Team, TeamAdmin)
