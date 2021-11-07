from django.contrib import admin

from community.models import (
        EnlacesAPI,
        Community_info,
        Link_Group
    )


@admin.register(Community_info)
class Community_infoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(EnlacesAPI)
class EnlacesAPIAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'FIELDNAME']


@admin.register(Link_Group)
class LinkGroupsAdmin(admin.ModelAdmin):
    list_display = ['url', 'name', 'created']
    readonly_fields = ('name', 'description', 'image', 'created')
