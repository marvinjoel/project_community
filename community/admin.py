from django.contrib import admin

from community.models import EnlacesAPI, Community_info, Groups


@admin.register(Community_info)
class Community_infoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(EnlacesAPI)
class EnlacesAPIAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'FIELDNAME']


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ['id', 'url']
    readonly_fields = ('name', 'description', 'image', 'created')
